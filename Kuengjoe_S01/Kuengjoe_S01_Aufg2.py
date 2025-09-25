
import numpy as np

# Beispiel-Aufruf (Aufgabe 2 / Polynom aus Aufg. 1):
# x, p, dp, Pint = Kuengjoe_S01_Aufg2([-105, 29, 110, -30, -5, 1], -10, 10)


def _as_1d_array(a):
    arr = np.asarray(a, dtype=float)
    if arr.size == 0:
        raise Exception("Fehler")
    if arr.ndim == 2:
        if 1 in arr.shape:
            arr = arr.reshape(-1)
        else:
            raise Exception("Fehler:")
    elif arr.ndim != 1:
        raise Exception("Fehler")
    return arr


def poly_derivate_coeffs(a):
    a = _as_1d_array(a)
    if a.size < 2:
        return np.array([0.0], dtype=float)
    dcoeffs = np.empty((a.size-1), dtype=float)
    for k in range(1, a.size):
            dcoeffs[k-1] = k * a[k]
    return dcoeffs

def poly_integrate_coeffs(a, C=0.0):
    a = _as_1d_array(a)
    if a.size < 1:
        return np.array([C], dtype=float)
    coeffs = np.empty(a.size+1, dtype=float)
    coeffs[0] = C
    for k in range(a.size):
        coeffs[k+1] = a[k] / (k + 1)

    return coeffs

def poly_eval(a, x):
    a = _as_1d_array(a)
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x, dtype=float)
    xpow = np.ones_like(x, dtype=float)
    for ak in a:
        y += ak * xpow
        xpow *= x
    return y

    #
    # Berechnet p(x), p'(x) und P(x) (mit C=0) für das Polynom mit Koeffizienten a0..an auf [xmin, xmax].
    #
    # Input:
    #   a     : Sequenz [a0, a1, ..., an] (vom konstanten Term bis Grad n)
    #   xmin  : Intervallanfang (xmin < xmax)
    #   xmax  : Intervallende
    #
    # Output:
    #   x     : äquidistante Stützstellen in [xmin, xmax]
    #   p     : Werte von p(x)
    #   dp    : Werte von p'(x)
    #   Pint  : Werte der Stammfunktion P(x) mit Integrationskonstante C=0
    #


def Kuengjoe_S01_Aufg2(a, xmin, xmax):

    a = _as_1d_array(a)

    if not np.isscalar(xmin) or not np.isscalar(xmax):
        raise Exception("Fehler")
    xmin = float(xmin); xmax = float(xmax)
    if not (xmin < xmax):
        raise Exception("Fehler")

    m = 1000
    x = np.linspace(xmin, xmax, m+1)

    d  = poly_derivate_coeffs(a)
    P  = poly_integrate_coeffs(a, C=0.0)


    p    = poly_eval(a, x)
    dp   = poly_eval(d, x)
    pint = poly_eval(P, x)

    return (x, p, dp, pint)