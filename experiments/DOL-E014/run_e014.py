#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
CONFIG=Path(__file__).with_name("config.json")
A=[-1,0,1]
def nxt(e,a,g,d,n): return float(np.clip(e+g*a-0.2+d+n,0,10))
def rew(e,a): return -abs(e-5)-0.05*abs(a)
def fit(rng,c):
 X=[];Y=[]
 for _ in range(c["training"]["episodes"]):
  e=float(rng.choice(c["training"]["initial_energy_values"]))
  for _ in range(c["training"]["steps_per_episode"]):
   a=int(rng.choice(A)); n=float(rng.normal(0,c["organism"]["noise_sd"]))
   en=nxt(e,a,0.55,0.2,n); X.append([1,e,a]);Y.append(en);e=en
 return np.linalg.lstsq(np.asarray(X),np.asarray(Y),rcond=None)[0]
def main():
 c=json.loads(CONFIG.read_text()); rng=np.random.default_rng(14014); beta=fit(rng,c); ghat=float(beta[2])
 sums={k:0. for k in ["self","reactive","damaged","oracle"]}; sq=0.;N=0
 for ep in range(c["held_out"]["episodes"]):
  e0=float(c["held_out"]["initial_energy_values"][ep%4]); noise=rng.normal(0,c["organism"]["noise_sd"],c["held_out"]["steps_per_episode"])
  s={k:e0 for k in sums}
  for z in noise:
   e=s["self"]; vals=[(rew(float(np.dot(beta,[1,e,a])),a),a) for a in A]; a=max(vals)[1]; en=nxt(e,a,ghat,-.2,float(z)); sums["self"]+=rew(en,a); sq+=(en-np.dot(beta,[1,e,a]))**2;N+=1;s["self"]=en
   e=s["reactive"]; a=1 if e<4.5 else (-1 if e>5.5 else 0); en=nxt(e,a,.55,-.2,float(z));sums["reactive"]+=rew(en,a);s["reactive"]=en
   e=s["damaged"]; vals=[(rew(float(e+1.0*a-0.2-.2),a),a) for a in A]; a=max(vals)[1]; en=nxt(e,a,1.0,-.2,float(z));sums["damaged"]+=rew(en,a);s["damaged"]=en
   e=s["oracle"]; vals=[(rew(nxt(e,a,.55,-.2,float(z)),a),a) for a in A];a=max(vals)[1];en=nxt(e,a,.55,-.2,float(z));sums["oracle"]+=rew(en,a);s["oracle"]=en
 avg={k:v/(c["held_out"]["episodes"]*c["held_out"]["steps_per_episode"]) for k,v in sums.items()};rmse=float(np.sqrt(sq/N));gap=avg["self"]-avg["reactive"];drop=avg["self"]-avg["damaged"];og=avg["oracle"]-avg["self"]
 print(json.dumps({"id":"DOL-E014","status":"EXECUTED","decision":"PENDING","results":{"mean_step_reward":avg,"learned_gain":ghat,"prediction_rmse":rmse,"self_model_gap":gap,"causal_drop":drop,"oracle_gap":og}},indent=2))
if __name__=="__main__":main()
