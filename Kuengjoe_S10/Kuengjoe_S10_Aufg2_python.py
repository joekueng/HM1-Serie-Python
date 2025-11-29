import numpy as np

A = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]], dtype=float)
b = np.array([19, 5, 34], dtype=float)
x_k = np.array([1, -1, 3], dtype=float)
U = np.triu(A, 1)
DL = np.tril(A)

DL_inv = np.linalg.inv(DL)

print(f"Startvektor x(0): {np.around(x_k, 4)}")
x_history = [x_k.copy()]

for k in range(1, 4):
    x_new = np.dot(DL_inv, (b - np.dot(U, x_k)))
    x_history.append(x_new.copy())
    x_k = x_new
    print(f"x({k}): {np.around(x_k, 4)}")

x_1 = np.array([2.7500, -1.4167, 3.5714])
x_2 = np.array([2.1190, -1.0873, 3.9780])
x_3 = np.array([1.9861, -0.9945, 4.0049])

print("-" * 35)
print(f"Näherung x(3) (4 Dezimalstellen): {x_3}")