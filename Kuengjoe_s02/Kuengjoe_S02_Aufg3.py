import math
import matplotlib.pyplot as plt

def s2n_naiv(s: float) -> float:
    t = max(0.0, 1.0 - (s*s)/4.0)
    return math.sqrt(2.0 - 2.0*math.sqrt(t))

def s2n_stabil(s: float) -> float:
    t = max(0.0, 1.0 - (s*s)/4.0)
    return s / math.sqrt(2.0*(1.0 + math.sqrt(t)))

n0 = 6
s_naiv = 1.0
s_stab = 1.0
K = 40

m_vals = [n0]
p_naiv = [n0 * s_naiv]
p_stab = [n0 * s_stab]

m = n0
for _ in range(K):
    m *= 2
    s_naiv = s2n_naiv(s_naiv)
    s_stab = s2n_stabil(s_stab)
    m_vals.append(m)
    p_naiv.append(m * s_naiv)
    p_stab.append(m * s_stab)

zwei_pi = 2.0 * math.pi
print(f"Letzter m-Wert:           m = {m_vals[-1]:.0f}")
print(f"Naiv:    m*s_m = {p_naiv[-1]:.15f}   Fehler = {abs(p_naiv[-1]-zwei_pi):.3e}")
print(f"Stabil:  m*s_m = {p_stab[-1]:.15f}   Fehler = {abs(p_stab[-1]-zwei_pi):.3e}")
err = abs(p_stab[-1] - 2*math.pi)/(2*math.pi)
print(f"relativer Fehler stabil = {err:.3e}")



plt.figure()
plt.plot(m_vals, p_naiv, label="naive Formel")
plt.plot(m_vals, p_stab, label="stabilisierte Formel")
plt.axhline(zwei_pi, linestyle="--", linewidth=1, label="2π")
plt.xscale("log")
plt.xlabel("Anzahl Ecken m (log-Skala)")
plt.ylabel("Umfangapproximation m·s_m")
plt.title("Archimedes-Algorithmus: Umfang des Einheitskreises")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
