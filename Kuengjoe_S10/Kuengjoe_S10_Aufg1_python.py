import numpy as np

A = np.array([[8, 5, 2],
              [5, 9, 1],
              [4, 2, 7]], dtype=float)

b = np.array([19, 5, 34], dtype=float)
x_start = np.array([1, -1, 3], dtype=float)
x_exact = np.array([2, -1, 4], dtype=float)

D = np.diag(np.diag(A))
L_plus_U = A - D
inv_D = np.linalg.inv(D)


B_jacobi = -np.dot(inv_D, L_plus_U)
alpha = np.linalg.norm(B_jacobi, np.inf)
#german text
print(f"Alpha (Faktor von Kontraktion): {alpha}")


x_curr = x_start.copy()
print(f"x(0) = {x_curr}")

x_history = [x_curr.copy()]

for k in range(1, 4):
    x_new = np.dot(inv_D, (b - np.dot(L_plus_U, x_curr)))

    print(f"x({k}) = {x_new}")
    x_history.append(x_new)
    x_curr = x_new

print("-" * 30)
print(f"Näherungslösung x(3): {np.around(x_curr, 4)}")