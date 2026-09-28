"""DOL-E002 C2 synthetic replication runner.

Fixed experiment:
- relation: 2 -> 7
- ON k=0.2
- CUT k=0
- RESTORE k=0.2
- perturb source 2 at t=10
- negative-control source 3
- seeds 1000..1099
"""
from __future__ import annotations
import numpy as np

T = 80
T0 = 10
NOISE = 0.03
K_ON = 0.2
K_CUT = 0.0
K_RESTORE = 0.2
WIN = slice(T0 + 1, T0 + 21)


def simulate(seed: int, k: float, perturb_source: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    noise = rng.normal(0.0, NOISE, (T, 10))
    x = np.zeros(10)
    y = np.zeros(10)
    target = []

    for t in range(T):
        x_old = x.copy()
        drive = np.zeros(10)
        if t == T0:
            drive[perturb_source] = 1.0

        x += -x / 5.0 + drive + noise[t]
        y += -y / 5.0 + k * x_old[2]
        target.append(y[7])

    return np.asarray(target)


def response(a: np.ndarray, baseline: np.ndarray) -> float:
    return float(np.sum(np.abs(a[WIN] - baseline[WIN])))


def main() -> None:
    rows = []

    for seed in range(1000, 1100):
        baseline = simulate(seed, K_CUT, 2)
        on = simulate(seed, K_ON, 2)
        cut = simulate(seed, K_CUT, 2)
        restore = simulate(seed, K_RESTORE, 2)
        negative = simulate(seed, K_ON, 3)

        rows.append([
            response(on, baseline),
            response(cut, baseline),
            response(restore, baseline),
            response(negative, baseline),
        ])

    m = np.asarray(rows)
    means = m.mean(axis=0)

    print("seeds=100")
    print(f"mean_on={means[0]:.8f}")
    print(f"mean_cut={means[1]:.8f}")
    print(f"mean_restore={means[2]:.8f}")
    print(f"mean_negative={means[3]:.8f}")
    print(f"cut_on_ratio={means[1]/means[0]:.8f}")
    print(f"restore_on_ratio={means[2]/means[0]:.8f}")
    print(f"on_negative_ratio={means[0]/means[3]:.8f}")
    print(f"seeds_on_gt_3x_negative={np.mean(m[:,0] > 3*m[:,3]):.8f}")


if __name__ == "__main__":
    main()
