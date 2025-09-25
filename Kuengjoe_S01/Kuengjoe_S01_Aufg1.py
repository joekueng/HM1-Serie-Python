import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


limr = 10  # Bereich für x-Achse
liml = -10

def f(x):
    return x**5 - 5*x**4 - 30*x**3 + 110*x**2 + 29*x - 105

def df(x):
    return 5*x**4 - 20*x**3 - 90*x**2 + 220*x + 29

def F(x):
    return (x**6)/6 - x**5 - (15/2)*x**4 + (110/3)*x**3 + (29/2)*x**2 - 105*x


x = np.linspace(liml, limr, 4000)
y = f(x)


plt.figure(figsize=(9, 6))
plt.plot(x, y, label='f(x)')
plt.plot(x, df(x), label="f'(x)")
plt.plot(x, F(x), label='F(x) (C=0)')

plt.ylim(-2500, 2500)
plt.xlim(liml, limr)


plt.title("Polinom f, Ableitung f' und Stammfunktion F auf einem gemeinsamen Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()


plt.show()