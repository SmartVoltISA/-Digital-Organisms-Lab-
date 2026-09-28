#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
CONFIG=Path(__file__).with_name("config.json")
def nxt(e,a,g,n): return float(np.clip(e+g*a-0.1+n,0,10))
def reward(en,a): return -abs(en-5)-0.30*a
def main():
 c=json.loads(CONFIG.read_text()); rng=np.random.default_rng(15015); X=[];Y=[]
 for _ in range(c["training"]["episodes"]):
  e=float(rng.choice(c["training"]["initial_energy_values"]))
  for _ in range(c["training"]["steps_per_episode"]):
   a=int(rng.integers(0,2)); n=float(rng.normal(0,c["organism"]["noise_sd"])); en=nxt(e,a,.55,n); X.append([1,e,a]);Y.append(en);e=en
 beta=np.linalg.lstsq(np.asarray(X),np.asarray(Y),rcond=None)[0]; ghat=float(beta[2])
 counts={k:[0,0] for k in ["self","reactive","damaged","oracle"]}; sq=0.;N=0
 states=c["held_out"]["states"]
 for e0 in states:
  for _ in range(c["held_out"]["episodes_per_state"]):
   noise=float(rng.normal(0,c["organism"]["noise_sd"]))
   true_vals=[(reward(nxt(e0,a,.55,noise),a),a) for a in [0,1]]; oracle=max(true_vals)[1]
   pred=[(reward(float(np.dot(beta,[1,e0,a])),a),a) for a in [0,1]]; ap=max(pred)[1]
   rp=1 if e0<4.475 else 0
   dp=max([(reward(float(e0+1.0*a-0.1),a),a) for a in [0,1]])[1]
   for k,a in [("self",ap),("reactive",rp),("damaged",dp),("oracle",oracle)]: counts[k][0]+=int(a==oracle);counts[k][1]+=1
   sq+=(nxt(e0,ap,.55,noise)-np.dot(beta,[1,e0,ap]))**2;N+=1
 acc={k:counts[k][0]/counts[k][1] for k in counts}; rmse=float(np.sqrt(sq/N))
 print(json.dumps({"id":"DOL-E015","status":"EXECUTED","decision":"PENDING","results":{"learned_gain":ghat,"accuracy":acc,"self_model_gap":acc["self"]-acc["reactive"],"causal_drop":acc["self"]-acc["damaged"],"prediction_rmse":rmse}},indent=2))
if __name__=="__main__":main()
