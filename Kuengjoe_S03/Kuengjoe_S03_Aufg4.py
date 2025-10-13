import numpy as np
import matplotlib.pyplot as plt

def g(x):
    # Naive Form des Polynoms 100 x² − 200 x + 99
    return 100*x**2 - 200*x + 99

def g_fact(x):
    # Faktorisierte Form 100 (x − 1.1)(x − 0.9) – vermeidet Auslöschung
    return 100*(x-1.1)*(x-0.9)

def h(x, factored=False):
    # Liefert h(x) = sqrt(g(x)); bei factored=True wird die stabile Variante
    # g_fact(x) verwendet
    return np.sqrt(g_fact(x) if factored else g(x))

def kappa_h(x):
    # Konditionszahl κ_h(x) = |x * h'(x) / h(x)|
    # mit h'(x) = 100 (x − 1) / h(x)
    return np.abs(x * 100*(x-1) / (h(x)**2))

# a) Vergleich der Auswertungen
x_test = 1.1 + np.array([1e-8, 1e-7, 1e-6, 1e-5])
print("x           h_naiv           h_fakt          relFehler")
for x in x_test:
    # instabile Auswertung
    h_naiv = h(x)
    # stabile Auswertungm
    h_fakt = h(x, factored=True)
    relerr = abs(h_naiv - h_fakt)/abs(h_fakt)
    print(f"{x:.10f}  {h_naiv:.12e}  {h_fakt:.12e}  {relerr:.2e}")

# b) Plot der Konditionszahl κ_h(x) auf [1.1, 1.3]
dx = 1e-7
x_vals = np.arange(1.1 + dx, 1.3 + dx, dx)
plt.semilogy(x_vals, kappa_h(x_vals))
plt.xlabel("x")
plt.ylabel(r"$\kappa_h(x)$")
plt.title("Konditionszahl von $h(x)$ auf [1.1, 1.3]")
plt.grid(True, which="both", ls="--", alpha=0.6)
plt.tight_layout()
plt.show()
