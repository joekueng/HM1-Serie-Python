

import math

def maschinengenauigkeit():
    eps = 1.0
    while 1.0 + eps != 1.0:
        eps /= 2.0
    return eps

def q_min_aus_eps(eps):
    q = 1.0/eps
    while 1.0 + q != q:
        q *= 2.0
    return q

eps = maschinengenauigkeit()
eps_krit = 2.0*eps
q_min = q_min_aus_eps(eps)

bits = round(-math.log2(eps))      # ≈ 53
decs = round(-math.log10(eps))

eps = maschinengenauigkeit()
eps_krit = 2.0 * eps         # kleinste Zahl mit 1+eps_krit != 1
q_min = q_min_aus_eps(eps)

bits = round(-math.log2(eps))     # ≈ 53
decs = round(-math.log10(eps))    # ≈ 16

print(f"Maschinengenauigkeit eps   = {eps:.20e}")
print(f"Kontrolle: 1+eps == 1      -> {1.0 + eps == 1.0}")
print(f"Kontrolle: 1+2*eps != 1    -> {1.0 + eps_krit != 1.0}")
print(f"Signifikanz: ~{bits} Bits (~{decs} Dezimalstellen)")
print(f"q_min                     = {q_min:.0f}")
print(f"Kontrolle: 1+q_min == q_min -> {1.0 + q_min == q_min}")
print("Zusammenhang: q_min = 1/eps (bei IEEE-754 double exakt).")