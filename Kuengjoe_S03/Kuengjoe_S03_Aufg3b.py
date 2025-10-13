
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 5.0 * (2.0 * x**2)**(-1.0/3.0)

def g(x):
    return 10.0**5 * (2.0 * np.e)**(-x/100.0)


def h_exp(x):
    return (625.0/64.0)**x

# (i)
x1 = np.logspace(-3, 2, 4000)  # 0.001 ... 100
y1 = f(x1)
plt.figure()
plt.loglog(x1, y1)
plt.title("Aufg. 3b (i) – f(x) as straight line in log-log")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True, which="both")

# (ii)
x2 = np.linspace(1e-6, 100.0, 4000)
y2 = g(x2)
plt.figure()
plt.semilogy(x2, y2)
plt.title("Aufg. 3b (ii) – g(x) as straight line in semilog-y")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.grid(True, which="both")

# (iii)
x3 = np.linspace(1e-6, 100.0, 4000)
y3 = h_exp(x3)
plt.figure()
plt.semilogy(x3, y3)
plt.title("Aufg. 3b (iii) – h(x) as straight line in semilog-y")
plt.xlabel("x")
plt.ylabel("h(x)")
plt.grid(True, which="both")

plt.show()
