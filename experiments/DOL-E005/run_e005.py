#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np

CONFIG=Path(__file__).with_name("config.json")

def trial(seed, cue, erase=False, sham=False):
    cfg=json.loads(CONFIG.read_text())
    noise_sd=cfg["model"]["noise_sd"]
    rng=np.random.default_rng(seed)
    noise=rng.normal(0,noise_sd,1000)
    x=0.0; m=0.0; i=0
    def step(e):
        nonlocal x,m,i
        x=0.05*x+0.4*e+0.005*m+noise[i]
        m=0.995*m+0.05*np.clip(e,-1,1)
        i+=1
        return x
    for _ in range(50): step(0)
    cue_value=0 if sham else cue
    for _ in range(20): step(cue_value)
    for _ in range(150): step(0)
    x=0.0
    if erase: m=0.0
    return float(np.mean(np.abs([step(0.2) for _ in range(10)])))

def main():
    cfg=json.loads(CONFIG.read_text())
    seeds=range(cfg["seeds"]["start"],cfg["seeds"]["start"]+cfg["seeds"]["count"])
    rows=[(trial(s,1),trial(s,-1),trial(s,1,True),trial(s,-1,True),trial(s,1,False,True),trial(s,-1,False,True)) for s in seeds]
    a,b,ea,eb,sa,sb=np.array(rows).T
    effect=np.abs(a-b)
    erase=np.abs(ea-eb)
    sham=np.abs(sa-sb)
    er=erase/np.maximum(effect,1e-12)
    sr=sham/np.maximum(effect,1e-12)
    result={
      "id":"DOL-E005","status":"EXECUTED","decision":"FAIL","n":len(rows),
      "seed_range":f'{cfg["seeds"]["start"]}-{cfg["seeds"]["start"]+cfg["seeds"]["count"]-1}',
      "mean_R_A":float(a.mean()),"mean_R_B":float(b.mean()),
      "mean_memory_effect":float(effect.mean()),
      "fraction_R_A_gt_R_B":float((a>b).mean()),
      "mean_erase_residual_ratio":float(er.mean()),
      "mean_sham_ratio":float(sr.mean()),
      "memory_effect_q05_q50_q95":[float(x) for x in np.quantile(effect,[.05,.5,.95])],
      "erase_ratio_q05_q50_q95":[float(x) for x in np.quantile(er,[.05,.5,.95])],
      "sham_ratio_q05_q50_q95":[float(x) for x in np.quantile(sr,[.05,.5,.95])],
      "checks":{
        "memory_effect":bool(effect.mean()>=.10),
        "direction":bool((a>b).mean()>=.95),
        "erase":bool(er.mean()<=.10),
        "sham":bool(sr.mean()<=.10)
      }
    }
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
