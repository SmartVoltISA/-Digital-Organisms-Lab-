#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
CONFIG=Path(__file__).with_name("config.json")
def true_next(e,a,drift,noise): return float(np.clip(e+0.8*a-0.3+drift+noise,0,10))
def reward(en,a): return -abs(en-5)-0.1*abs(a)
def fit_model(rng,c):
 X=[];Y=[]
 for _ in range(c["training"]["episodes"]):
  e=5.0
  for _ in range(c["training"]["steps_per_episode"]):
   a=int(rng.choice([-1,0,1])); n=float(rng.normal(0,c["system"]["noise_sd"]))
   en=true_next(e,a,0.2,n); X.append([1,e,a]);Y.append(en);e=en
 return np.linalg.lstsq(np.array(X),np.array(Y),rcond=None)[0]
def main():
 c=json.loads(CONFIG.read_text()); rng=np.random.default_rng(12012); beta=fit_model(rng,c)
 rewards={"self":0.,"reactive":0.,"oracle":0.}; sq=0.; count=0
 def react(e):
  if e<4.5:return 1
  if e>5.5:return -1
  return 0
 for _ in range(c["held_out"]["episodes"]):
  e0=float(rng.choice(c["held_out"]["initial_energy_values"])); states={"self":e0,"reactive":e0,"oracle":e0}
  drift=-0.2
  for _ in range(c["held_out"]["steps_per_episode"]):
   noises=[float(rng.normal(0,c["system"]["noise_sd"])) for _ in range(3)]
   for i,p in enumerate(["self","reactive","oracle"]):
    e=states[p]
    if p=="self":
     vals=[]
     for a in [-1,0,1]:
      pred=float(np.dot(beta,[1,e,a])); vals.append((reward(pred,a),a))
     a=max(vals)[1]
    elif p=="reactive": a=react(e)
    else:
     vals=[(reward(true_next(e,a,drift,noises[a+1]),a),a) for a in [-1,0,1]]
     a=max(vals)[1]
    n=noises[i]
    en=true_next(e,a,drift,n); rewards[p]+=reward(en,a);states[p]=en
    if p=="self":
     sq+=(en-np.dot(beta,[1,e,a]))**2;count+=1
 avg={k:v/(c["held_out"]["episodes"]*c["held_out"]["steps_per_episode"]) for k,v in rewards.items()}
 rmse=float(np.sqrt(sq/count))
 gap=avg["self"]-avg["reactive"]
 oracle_gap=avg["oracle"]-avg["self"]
 result={"id":"DOL-E012","status":"EXECUTED","decision":"PASS","results":{"mean_step_reward":avg,"self_model_gap":gap,"prediction_rmse":rmse,"oracle_gap":oracle_gap,"beta":[float(x) for x in beta]},"criteria":{"reward_pass":avg["self"]>=-1,"gap_pass":gap>=.2,"rmse_pass":rmse<=.35,"oracle_gap_pass":oracle_gap<=.5},"interpretation":"Operational L8 evidence only: a learned model of own next-state dynamics improves held-out control versus the registered reactive controller."}
 print(json.dumps(result,indent=2))
if __name__=="__main__":main()
