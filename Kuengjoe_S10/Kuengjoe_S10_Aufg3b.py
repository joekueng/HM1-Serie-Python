import numpy as np
import matplotlib.pyplot as plt
import time
from Kuengjoe_S10_Aufg3a import Kuengjoe_S10_Aufg3a

print("Datenerzeugung läuft (dim=3000)... bitte warten.")
dim = 3000

A = np.diag(np.diag(np.ones((dim, dim)) * 4000)) + np.ones((dim, dim))

dum1 = np.arange(1, int(dim/2 + 1), dtype=np.float64).reshape((int(dim/2), 1))
dum2 = np.arange(int(dim/2), 0, -1, dtype=np.float64).reshape((int(dim/2), 1))

x_exact = np.append(dum1, dum2, axis=0)

b = np.dot(A, x_exact)

x0 = np.zeros((dim, 1))
tol = 1e-4


# A) Jacobi-Verfahren
print("\nStarte Jacobi-Verfahren...")
start_time = time.time()
xn_jac, n_jac, n2_jac = Kuengjoe_S10_Aufg3a(A, b, x0, tol, 'Jacobi')
time_jac = time.time() - start_time
print(f"Jacobi: {time_jac:.4f} sek | Iterationen: {n_jac} (A-priori: {n2_jac})")

# B) Gauss-Seidel-Verfahren
print("\nStarte Gauss-Seidel-Verfahren...")
start_time = time.time()
xn_gs, n_gs, n2_gs = Kuengjoe_S10_Aufg3a(A, b, x0, tol, 'Gauss-Seidel')
time_gs = time.time() - start_time
print(f"Gauss-Seidel: {time_gs:.4f} sek | Iterationen: {n_gs} (A-priori: {n2_gs})")


print("\nStarte Gauss-Verfahren (Numpy linalg.solve)...")
start_time = time.time()
xn_gauss = np.linalg.solve(A, b)
time_gauss = time.time() - start_time
print(f"Gauss (Numpy): {time_gauss:.4f} sek")


"""
KOMMENTAR ZU TEIL B:
Ein manuelles Gauss-Verfahren (mit Python-Schleifen) wäre bei dim=3000 extrem langsam.
Da ich hier aber np.linalg.solve (optimierter C-Code) benutze, ist Gauss hier
schneller als Gauss-Seidel.

A manual Gauss method (using Python loops) would be extremely slow for dim=3000.
However, since I use np.linalg.solve (optimized C code) here, Gauss appears 
faster than Gauss-Seidel in this test.
"""


err_jac = np.abs(xn_jac - x_exact)
err_gs = np.abs(xn_gs - x_exact)
err_gauss = np.abs(xn_gauss - x_exact)

plt.figure(figsize=(10, 6))

plt.plot(err_jac, label='Fehler Jacobi', color='blue', alpha=0.7)
plt.plot(err_gs, label='Fehler Gauss-Seidel', color='red', alpha=0.7)
plt.plot(err_gauss, label='Fehler Gauss (Exakt)', color='green', alpha=0.7)

plt.title(f"Vergleich der absoluten Fehler (Dim={dim})")
plt.xlabel("Index des Vektorelements")
plt.ylabel("Absoluter Fehler |x_berechnet - x_exakt|")
plt.yscale('log')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.4)
plt.show()

print("\n--- Beobachtungen (Teil C) ---")
print("1. Der Fehler des Gauss-Verfahrens (direkter Löser) liegt im Bereich der Maschinengenauigkeit (ca. 1e-15).")
print("2. Die iterativen Verfahren (Jacobi, GS) stoppen, sobald die Fehlertoleranz (tol=1e-4) erreicht ist.")
print("3. Gauss-Seidel konvergiert typischerweise schneller (weniger Iterationen) als Jacobi.")