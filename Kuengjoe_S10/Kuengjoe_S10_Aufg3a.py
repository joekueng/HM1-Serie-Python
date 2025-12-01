import numpy as np
from numpy.linalg import norm

def Kuengjoe_S10_Aufg3a(A, b, x0, tol, opt):
    dim = A.shape[0]

    D_vec= np.diag(A)
    D = np.diag(D_vec)
    L = np.tril(A, -1)
    U = np.triu(A, 1)

    if  opt == 'Jacobi':
        inv_D = np.diag(1.0 / D_vec)

        B = -np.dot(inv_D, (L + U))
        c = np.dot(inv_D, b)

        del inv_D, L, U, D,

    elif opt == 'Gauss-Seidel':
        DL = D + L
        inv_DL = np.linalg.inv(DL)

        B = -np.dot(inv_DL, U)
        c = np.dot(inv_DL, b)

        del inv_DL, U, D, L,

    else:
        raise ValueError("Ungültige Option. Wählen Sie 'Jacobi' oder 'Gauss-Seidel'.")

    norm_B = norm(B, np.inf)

    x = x0.copy()
    x1 = np.dot(B, x) + c
    diff_x1_x0 = norm(x1 - x0, np.inf)


    if norm_B < 1.0 and diff_x1_x0 > 0:
        numerator = np.log((tol * (1 - norm_B)) / diff_x1_x0)
        denominator = np.log(norm_B)
        n2 = int(np.ceil(numerator / denominator))

    else:
        n2 = -1
    n = 0
    current_diff = tol +1

    x = x1
    n = 1

    while current_diff > tol and n < 10000:
        x_new = np.dot(B, x) + c
        current_diff = norm(x_new - x, np.inf)
        x = x_new
        n += 1
    xn = x
    return xn, n, n2