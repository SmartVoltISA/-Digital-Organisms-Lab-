#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
CONFIG=Path(__file__).with_name("config.json")

def run(seed,cue,delay,erase=False,sham=False):
    cfg=json.loads(CONFIG.read_text()); rng=np.random.default_rng(seed)
    noise=rng.normal(0,cfg["model"]["noise_sd"],5000); x=0.; m=0.; i=0
    def step(e):
        nonlocal x,m,i
        x=.05*x+.4*e+.005*m+noise[i]; m=.995*m+.05*np.clip(e,-1,1); i+=1; return x
    for _ in range(50): step(0)
    cv=0 if sham else cue
    for _ in range(20): step(cv)
    for _ in range(delay): step(0)
    x=0
    if erase: m=0
    return float(np.mean(np.abs([step(.2) for _ in range(10)])))
def main():
    c=json.loads(CONFIG.read_text()); delays=c["schedule"]["washout_delays"]
    seeds=list(range(c["seeds"]["start"],c["seeds"]["start"]+c["seeds"]["count"]))
    out={}
    for d in delays:
        a=np.array([run(s,1,d) for s in seeds]); b=np.array([run(s,-1,d) for s in seeds])
        ea=np.array([run(s,1,d,True) for s in seeds]); eb=np.array([run(s,-1,d,True) for s in seeds])
        sa=np.array([run(s,1,d,False,True) for s in seeds]); sb=np.array([run(s,-1,d,False,True) for s in seeds])
        eff=np.abs(a-b); er=np.abs(ea-eb)/np.maximum(eff,1e-12); sr=np.abs(sa-sb)/np.maximum(eff,1e-12)
        out[str(d)]={"memory_effect":float(eff.mean()),"retention":None,"fraction_A_gt_B":float((a>b).mean()),"erase_ratio":float(er.mean()),"sham_ratio":float(sr.mean())}
    base=out[str(delays[0])]["memory_effect"]
    for d in delays: out[str(d)]["retention"]=out[str(d)]["memory_effect"]/max(base,1e-12)
    vals=[out[str(d)]["memory_effect"] for d in delays]
    mono=all(vals[i+1] <= vals[i]+c["criteria"]["monotonic_tolerance"] for i in range(len(vals)-1))
    erase_ok=all(out[str(d)]["erase_ratio"]<=.1 for d in delays)
    sham_ok=all(out[str(d)]["sham_ratio"]<=.1 for d in delays)
    result={"id":"DOL-E006","status":"EXECUTED","decision":"FAIL","delays":delays,"results":out,
            "memory_effect_at_zero":base,"monotonic":mono,"erase_all_pass":erase_ok,"sham_all_pass":sham_ok,
            "criteria":{"zero_effect_pass":base>=.1,"monotonic_pass":mono,"erase_pass":erase_ok,"sham_pass":sham_ok}}
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
