import numpy as np
import matplotlib.pyplot as plt

# a)

def f1(x):
    return (((((((x - 14)*x + 84)*x - 280)*x + 560)*x - 672)*x + 448)*x - 128)

def f2(x):
    return (x-2)**7

xa = np.linspace(1.99, 2.01, 501, dtype=np.float64)

ya1 = f1(xa)
ya2 = f2(xa)

plt.figure()
plt.plot(xa, ya1, label='f1(x) expanded', linewidth=2)
plt.plot(xa, ya2, label='f2(x) (x-2)^7', linestyle='--', linewidth=2)
plt.title("Vergleich zweier äquivalenter Funktionen")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()



with np.errstate(divide='ignore', invalid='ignore'):
    rel_err= np.abs((ya1 - ya2)/ np.where( ya2!= 0, ya2, 1))

plt.figure()
plt.plot(xa, rel_err)
plt.title("Relativer Fehler zwischen f1 und f2")
plt.xlabel("x")
plt.ylabel("Relativer Fehler")
plt.yscale("log")
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()

# b)
xmin, xmax, h =  -1e-14, 1e-14, 1e-17
n = int(round((xmax - xmin) / h)) + 1
xb = np.linspace(xmin, xmax, n, dtype=np.float64)

def g_naive(x):
    return x / (np.sin(1.0+x) - np.sin(1.0))

g_b = g_naive(xb)
i0 = np.argmin(np.abs(xb))
g_b[i0] = np.nan


plt.figure()
plt.plot(xb, g_b)
plt.title('g(x) = x / (sin(1+x) - sin(1))')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid(True, alpha=0.3)
plt.tight_layout()


# c)

def g_stab(x):
    return x / (2.0 * np.cos(1.0 +0.5*x) * np.sin(0.5*x))

g_c = g_stab(xb)
g_c[i0] = 1.0 / np.cos(1.0)

plt.figure()
plt.plot(xb, g_c)
plt.axhline(1.0 /np.cos(1.0), linestyle='--')
plt.title('Stabilisierte Berechnung von g(x)')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid(True, alpha=0.3)
plt.tight_layout()

print('theoretischer Grenzwert: g(0) =', 1.0 / np.cos(1.0))

plt.show()






