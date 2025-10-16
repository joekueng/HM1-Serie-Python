import numpy as np

def f(k: float, a: float) -> float:
    return a * k *(1-k)

def iterate(a: float, k0: float= 0.1, steps: int = 100) -> float:
    k = k0
    for _ in range(steps):
        k = f(k, a)
    return k

alphas = np.arange(0.0, 4.01, 0.1)
print("α\tk_end\t\tFixpunkte (theoretisch)")
for alpha in alphas:
    k_num = iterate(alpha)
    k_fix1 = 0
    if alpha <= 1:
        k_fix2 = None
    else:
        k_fix2 = 1-1 / alpha

    print(f"{alpha:3.1f}\t{k_num:7.4f}\t{k_fix1}", end="")
    if k_fix2 is not None:
        print(f", {k_fix2:.4f}")
    else:
        print("")
