#!/usr/bin/env python3
import json, math
from pathlib import Path
import numpy as np

CONFIG = Path(__file__).with_name("config.json")

def trial(seed, trained=True):
    rng=np.random.default_rng(seed)
    noise=rng.normal(0,0.005,1000)
    i=0; x=0.0; a=0.0
    def step(e):
        nonlocal x,a,i
        x=0.8*x+0.6*e-0.4*a+noise[i]
        a=0.98*a+0.08*np.clip(e,-1,1)
        y=x+0.4*a
        i+=1
        return y
    for _ in range(50): step(0)
    pre=np.mean([abs(step(.5)) for _ in range(10)])
    if trained:
        for _ in range(20):
            for _ in range(5): step(1)
            for _ in range(5): step(0)
    else:
        for _ in range(200): step(0)
    for _ in range(50): step(0)
    post=np.mean([abs(step(.5)) for _ in range(10)])
    if trained:
        for _ in range(20):
            for _ in range(5): step(-1)
            for _ in range(5): step(0)
        for _ in range(50): step(0)
        rev=np.mean([abs(step(.5)) for _ in range(10)])
    else:
        rev=float("nan")
    return pre,post,rev

def main():
    cfg=json.loads(CONFIG.read_text())
    seeds=range(cfg["seeds"]["start"], cfg["seeds"]["start"]+cfg["seeds"]["count"])
    trained=np.array([trial(s,True) for s in seeds])
    control=np.array([trial(s,False) for s in seeds])
    ai=(trained[:,0]-trained[:,1])/np.maximum(trained[:,0],1e-12)
    rr=(trained[:,2]-trained[:,1])/np.maximum(trained[:,1],1e-12)
    ci=(control[:,0]-control[:,1])/np.maximum(control[:,0],1e-12)
    result={
      "n":len(list(seeds)),
      "mean_pre":float(trained[:,0].mean()),
      "mean_post":float(trained[:,1].mean()),
      "mean_reversal_probe":float(trained[:,2].mean()),
      "mean_adaptation_index":float(ai.mean()),
      "mean_reversal_recovery_index":float(rr.mean()),
      "mean_abs_no_training_index":float(np.abs(ci).mean()),
      "fraction_adaptation_ge_0.20":float((ai>=0.20).mean()),
      "fraction_reversal_recovery_ge_0.50":float((rr>=0.50).mean()),
      "fraction_no_training_abs_le_0.05":float((np.abs(ci)<=0.05).mean()),
      "adaptation_index_q05_q50_q95":[float(x) for x in np.quantile(ai,[.05,.5,.95])],
      "reversal_recovery_q05_q50_q95":[float(x) for x in np.quantile(rr,[.05,.5,.95])],
      "decision":"PASS"
    }
    assert result["mean_adaptation_index"]>=0.20
    assert result["mean_abs_no_training_index"]<=0.05
    assert result["mean_reversal_recovery_index"]>=0.50
    assert result["fraction_adaptation_ge_0.20"]>=0.95
    assert result["fraction_reversal_recovery_ge_0.50"]>=0.95
    assert result["fraction_no_training_abs_le_0.05"]>=0.95
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
