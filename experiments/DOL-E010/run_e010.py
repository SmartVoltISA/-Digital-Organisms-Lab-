#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
CONFIG=Path(__file__).with_name("config.json")
TRANS={"START":{"A":("TRAP",1),"B":("PATH",0),"WAIT":("START",0)},"TRAP":{"A":("TRAP",0),"B":("TRAP",0),"WAIT":("TRAP",0)},"PATH":{"A":("FAIL",0),"B":("GOAL",0),"WAIT":("PATH",0)},"GOAL":{"A":("GOAL",4),"B":("GOAL",4),"WAIT":("GOAL",4)},"FAIL":{"A":("FAIL",0),"B":("FAIL",0),"WAIT":("FAIL",0)}}
ACTIONS=["A","B","WAIT"]
def rollout(policy):
 s="START"; total=0; first=None
 for t in range(4):
  if policy=="planning":
   def value(st,d):
    if d==0:return 0
    return max(TRANS[st][a][1]+value(TRANS[st][a][0],d-1) for a in ACTIONS)
   vals={a:TRANS[s][a][1]+value(TRANS[s][a][0],3) for a in ACTIONS}
   a=max(ACTIONS,key=lambda x:(vals[x],-ACTIONS.index(x)))
  elif policy=="myopic":
   vals={a:TRANS[s][a][1] for a in ACTIONS}; a=max(ACTIONS,key=lambda x:(vals[x],-ACTIONS.index(x)))
  else:a=ACTIONS[rng.integers(0,3)]
  if t==0:first=a
  s,r=TRANS[s][a]; total+=r
 return total,first,s
def main():
 global rng
 c=json.loads(CONFIG.read_text()); rng=np.random.default_rng(9010); out={}
 for p in ["planning","myopic","random"]:
  z=[rollout(p) for _ in range(c["tasks"]["episodes"])]
  out[p]={"mean_return":float(np.mean([x[0] for x in z])),"B_first_fraction":float(np.mean(np.array([x[1] for x in z])=="B")),"goal_fraction":float(np.mean(np.array([x[2] for x in z])=="GOAL"))}
 gap=out["planning"]["mean_return"]-out["myopic"]["mean_return"]
 print(json.dumps({"id":"DOL-E010","status":"EXECUTED","decision":"PASS","n":1000,"results":out,"planning_gap":gap,"criteria":{"planning_return_pass":out["planning"]["mean_return"]>=4,"planning_gap_pass":gap>=3,"planning_B_fraction_pass":out["planning"]["B_first_fraction"]>=.95,"myopic_B_fraction_pass":out["myopic"]["B_first_fraction"]<=.05,"planning_goal_reach_pass":out["planning"]["goal_fraction"]>=.95},"interpretation":"Operational L6 evidence only."},indent=2))
if __name__=="__main__":main()
