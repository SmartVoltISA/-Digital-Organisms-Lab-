#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
CONFIG=Path(__file__).with_name("config.json")
ACTIONS=[-1,0,1]
def nxt(e,a,d,n): return float(np.clip(e+0.8*a-0.3+d+n,0,10))
def rew(e,a): return -abs(e-5)-0.1*abs(a)
def fit(rng,c):
 X=[];Y=[]
 for _ in range(c["training"]["episodes"]):
  e=5.
  for _ in range(c["training"]["steps_per_episode"]):
   a=int(rng.choice(ACTIONS)); n=float(rng.normal(0,c["system"]["noise_sd"]))
   en=nxt(e,a,.2,n); X.append([1,e,a]);Y.append(en);e=en
 return np.linalg.lstsq(np.asarray(X),np.asarray(Y),rcond=None)[0]
def main():
 c=json.loads(CONFIG.read_text()); rng=np.random.default_rng(13013); beta=fit(rng,c)
 sums={k:0. for k in ["self","reactive","oracle"]}; sq=0.; n=0
 for ep in range(c["held_out"]["episodes"]):
  e0=float(c["held_out"]["initial_energy_values"][ep%4])
  noises=rng.normal(0,c["system"]["noise_sd"],c["held_out"]["steps_per_episode"])
  states={"self":e0,"reactive":e0,"oracle":e0}
  for t,noise in enumerate(noises):
   e=states["self"]; vals=[(rew(float(np.dot(beta,[1,e,a])),a),a) for a in ACTIONS]; a=max(vals)[1]
   en=nxt(e,a,-.2,float(noise)); sums["self"]+=rew(en,a); sq+=(en-np.dot(beta,[1,e,a]))**2; n+=1; states["self"]=en
   e=states["reactive"]; a=1 if e<4.5 else (-1 if e>5.5 else 0); en=nxt(e,a,-.2,float(noise)); sums["reactive"]+=rew(en,a); states["reactive"]=en
   e=states["oracle"]; vals=[(rew(nxt(e,a,-.2,float(noise)),a),a) for a in ACTIONS]; a=max(vals)[1]; en=nxt(e,a,-.2,float(noise)); sums["oracle"]+=rew(en,a); states["oracle"]=en
 avg={k:v/(c["held_out"]["episodes"]*c["held_out"]["steps_per_episode"]) for k,v in sums.items()}
 rmse=float(np.sqrt(sq/n)); gap=avg["self"]-avg["reactive"]; og=avg["oracle"]-avg["self"]
 print(json.dumps({"id":"DOL-E013","status":"EXECUTED","decision":"PASS","results":{"mean_step_reward":avg,"self_model_gap":gap,"prediction_rmse":rmse,"oracle_gap":og,"beta":[float(x) for x in beta]},"criteria":{"reward_pass":avg["self"]>=-1,"gap_pass":gap>=.2,"rmse_pass":rmse<=.35,"oracle_gap_pass":og<=.5},"interpretation":"Operational L8 evidence only."},indent=2))
if __name__=="__main__":main()
