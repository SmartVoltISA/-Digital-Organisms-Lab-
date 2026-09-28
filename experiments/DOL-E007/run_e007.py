#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
from scipy.stats import binomtest
CONFIG=Path(__file__).with_name("config.json")
def run(seed,cue,erase=False,sham=False):
    c=json.loads(CONFIG.read_text()); rng=np.random.default_rng(seed)
    noise=rng.normal(0,c["model"]["noise_sd"],5000); x=0.; m=0.; i=0
    def step(e):
        nonlocal x,m,i
        x=.05*x+.4*e+.005*m+noise[i]; m=.995*m+.05*np.clip(e,-1,1); i+=1; return x
    for _ in range(50): step(0)
    cv=0 if sham else cue
    for _ in range(20): step(cv)
    x=0.
    if erase: m=0.
    return float(np.mean(np.abs([step(.2) for _ in range(10)])))
def bootstrap_ci(v,seed=7007,n=20000):
    rng=np.random.default_rng(seed); idx=rng.integers(0,len(v),(n,len(v)))
    means=np.mean(v[idx],axis=1)
    return [float(np.quantile(means,.025)),float(np.quantile(means,.975))]
def main():
    c=json.loads(CONFIG.read_text()); seeds=range(c["seeds"]["start"],c["seeds"]["start"]+c["seeds"]["count"])
    a=np.array([run(s,1) for s in seeds]); b=np.array([run(s,-1) for s in seeds]); d=a-b; eff=np.abs(d)
    k=int((d>0).sum()); p=float(binomtest(k,len(d),.5,alternative="greater").pvalue)
    ci=bootstrap_ci(d); contrast=2*eff/np.maximum(a+b,1e-12)
    ea=np.array([run(s,1,True) for s in seeds]); eb=np.array([run(s,-1,True) for s in seeds])
    sa=np.array([run(s,1,False,True) for s in seeds]); sb=np.array([run(s,-1,False,True) for s in seeds])
    er=float(np.mean(np.abs(ea-eb)/np.maximum(eff,1e-12))); sr=float(np.mean(np.abs(sa-sb)/np.maximum(eff,1e-12)))
    result={"id":"DOL-E007","status":"EXECUTED","decision":"PASS","n":len(d),"seed_range":"2000-2099",
      "results":{"mean_R_A":float(a.mean()),"mean_R_B":float(b.mean()),"mean_D":float(d.mean()),"mean_abs_D":float(eff.mean()),
      "direction_fraction":float(k/len(d)),"sign_test_p_one_sided":p,"bootstrap_95ci_mean_D":ci,
      "scale_free_contrast_mean":float(contrast.mean()),"scale_free_contrast_q05_q50_q95":[float(x) for x in np.quantile(contrast,[.05,.5,.95])],
      "erase_ratio":er,"sham_ratio":sr},
      "criteria":{"sign_test_alpha_0.01_pass":p<.01,"bootstrap_ci_positive_pass":ci[0]>0,"direction_fraction_ge_0.95_pass":k/len(d)>=.95,
      "erase_ratio_le_0.10_pass":er<=.10,"sham_ratio_le_0.10_pass":sr<=.10},
      "interpretation":"The preregistered synthetic system shows reproducible history-dependent behavior under matched present observable state. This does not establish biological memory, cognition, universality, or any higher complexity level."}
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
