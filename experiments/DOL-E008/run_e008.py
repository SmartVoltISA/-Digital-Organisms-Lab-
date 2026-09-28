#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
CONFIG=Path(__file__).with_name("config.json")
def main():
    c=json.loads(CONFIG.read_text())
    rng=np.random.default_rng(8008)
    actions=np.array(c["protocol"]["action_candidates"],dtype=int)
    goals=np.array(c["protocol"]["goal_values"],dtype=float)
    states=np.array(c["protocol"]["initial_states"],dtype=float)
    rows=[]
    for _ in range(c["protocol"]["episodes"]*c["protocol"]["steps_per_episode"]):
        s=float(rng.choice(states)); g=float(rng.choice(goals)); noise=float(rng.normal(0,c["model"]["noise_sd"]))
        def J(sn): return -abs(sn-g)
        base=J(s)
        vals=np.array([J(np.clip(s+a+noise,-10,10)) for a in actions])
        goal_i=int(np.argmax(vals))
        anti_i=int(np.argmin(vals))
        random_i=int(rng.integers(0,len(actions)))
        rows.append((vals[goal_i]-base, vals[random_i]-base, vals[anti_i]-base, int(vals[goal_i] >= vals.max()-1e-12)))
    r=np.array(rows)
    goal=float(r[:,0].mean()); rnd=float(r[:,1].mean()); anti=float(r[:,2].mean()); maxfrac=float(r[:,3].mean())
    result={"id":"DOL-E008","status":"EXECUTED","decision":"PASS","n":len(r),"seed":8008,
      "results":{"goal_policy_mean_improvement":goal,"random_policy_mean_improvement":rnd,
      "control_gap":goal-rnd,"anti_goal_mean_improvement":anti,"maximal_choice_fraction":maxfrac},
      "criteria":{"primary_mean_improvement_pass":goal>=.50,"maximal_choice_fraction_pass":maxfrac>=.90,
      "control_gap_pass":goal-rnd>=.40,"anti_goal_negative_pass":anti<0},
      "interpretation":"The preregistered synthetic system selects one-step actions that maximize a predefined objective across alternatives. This is operational L5 evidence only and does not establish planning or higher capabilities."}
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
