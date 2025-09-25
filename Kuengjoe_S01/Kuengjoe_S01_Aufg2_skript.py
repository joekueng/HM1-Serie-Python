# Name_S01_Aufg2_skript.py
import numpy as np
import matplotlib.pyplot as plt
from Kuengjoe_S01_Aufg2 import Kuengjoe_S01_Aufg2

if __name__ == "__main__":
    # Reproduktion der Abbildung aus Aufgabe 1: gleiches Polynom und Intervall
    a = [-105, 29, 110, -30, -5, 1]  # a0..a5 für f(x)=x^5-5x^4-30x^3+110x^2+29x-105
    xmin, xmax = -10, 10

    x, p, dp, pint = Kuengjoe_S01_Aufg2(a, xmin, xmax)

    plt.figure()
    plt.plot(x, p, label="p(x)")
    plt.plot(x, dp, label="p'(x)", linestyle="--")
    plt.plot(x, pint, label="P(x) (C=0)", linestyle=":")
    plt.ylim(-2500, 2500)
    plt.xlabel("x")
    plt.xlabel("x")
    plt.ylabel("Wert")
    plt.title("Polynom, Ableitung und Stammfunktion")
    plt.grid(True)
    plt.legend()
    plt.show()
