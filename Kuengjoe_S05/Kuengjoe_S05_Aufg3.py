import math

# Das Newton-Verfahren erfordert die Ableitung von f; ist f' schwer zu bestimmen oder fast Null,
# kann das Verfahren instabil und rechenaufwendig werden.


def secant_method(f, x0, x1, tol=1e-10, max_iter=100):

    for _ in range(max_iter):
        if abs(x1 - x0) < tol:
            return x1
        f_x0 = f(x0)
        f_x1 = f(x1)
        if abs(f_x1) < tol:
            return x1
        if abs(f_x1 - f_x0) < 1e-14:
            raise ZeroDivisionError("Sekantenmethode: Division durch Null. Sekanten instabil.")
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x2
    if abs(x1 - x0) < tol:
        return x1
    if abs(x1 - x0) < 1e-14:
        raise ValueError("Sekantenmethode konvergiert nicht ausreichend.")
    return None


f = lambda x: math.exp(x**2) + x** -3 - 10.0
root1 = secant_method(f, 1.0, 2.0)
print(f"Gefundene Nullstelle in [1, 2]: {root1:.10f}, f(root1) = {f(root1):.3e}")

root2 = secant_method(f, 0.4, 0.6)
print(f"Gefundene Nullstelle in [0.4, 0.6]: {root2:.10f}, f(root2) = {f(root2):.3e}")

root3 = secant_method(f, -1.0, -1.2)
print(f"Gefundene Nullstelle in [-1, 0]: {root3:.10f}, f(root3) = {f(root3):.3e}")


R = 5.0
g = lambda h: math.pi *h ** 2 * (3.0 * R - h) / 3.0 - 471.0

root_h = secant_method(g, 4.0, 5.0)
print(f"Gefundene Höhe h für Volumen 471: {root_h:.10f}, g(h) = {g(root_h):.3e}")


