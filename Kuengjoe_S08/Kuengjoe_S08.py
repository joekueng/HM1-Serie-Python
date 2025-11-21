import numpy as np
import timeit

def qr_zerlegung_gram_schmidt(matrix_a):
    matrix_a = np.array(matrix_a, dtype=float)
    number_of_rows, number_of_columns = matrix_a.shape

    matrix_q = np.zeros((number_of_rows, number_of_columns), dtype=float)
    matrix_r = np.zeros((number_of_columns, number_of_columns), dtype=float)

    for i in range (number_of_columns):
        v_i = matrix_a[:, i].copy()

        for j in range(i):
            r_ji = np.dot(matrix_q[:, j], matrix_a[:, i])
            matrix_r[j, i] = r_ji
            v_i -= r_ji * matrix_q[:, j]

        r_ii = np.linalg.norm(v_i)
        if r_ii < 1e-12:
            raise ValueError("Die Spalten von A sind linear abhängig.")
        matrix_r[i, i] = r_ii
        matrix_q[:, i] = v_i / r_ii

    return matrix_q, matrix_r




def Kuengjoe_S08_Aufg2(matrix_a):
    matrix_q, matrix_r = qr_zerlegung_gram_schmidt(matrix_a)

    matrix_a = np.array(matrix_a, dtype=float)
    reconstruction_error = np.linalg.norm(matrix_a - matrix_q @ matrix_r)
    orthogonality_error = np.linalg.norm(
        matrix_q.T @ matrix_q - np.eye(matrix_q.shape[1])
    )

    print("Kontrolle fuer Kuengjoe_S08_Aufg2:")
    print("  ||A - Q R||_F        =", reconstruction_error)
    print("  ||Q^T Q - I||_F      =", orthogonality_error)

    return matrix_q, matrix_r


if __name__ == "__main__":
    A_aufgabe1_example = np.array(
        [
            [2.0, -1.0, 0.0],
            [-1.0, 2.0, -1.0],
            [0.0, -1.0, 2.0],
        ],
        dtype=float,
    )

    print("=== QR-Zerlegung mit Gram-Schmidt (Kuengjoe_S08_Aufg2) ===")
    Q_example, R_example = Kuengjoe_S08_Aufg2(A_aufgabe1_example)
    print("Q =")
    print(Q_example)
    print("R =")
    print(R_example)
    print()

    A = A_aufgabe1_example  # Kuengjoe A gemäss Aufgabenblatt

    print("=== Laufzeitvergleich fuer Matrix A (Aufgabe 1) ===")

    t1 = timeit.repeat(
        "Kuengjoe_S08_Aufg2(A)",
        "from __main__ import Kuengjoe_S08_Aufg2, A",
        number=100,
    )

    t2 = timeit.repeat(
        "np.linalg.qr(A)",
        "from __main__ import np, A",
        number=100,
    )

    average_time_Kuengjoe_s08 = np.average(t1) / 100.0
    average_time_numpy_qr = np.average(t2) / 100.0

    print("Durchschnittszeit eigene QR (Kuengjoe_S08_Aufg2):", average_time_Kuengjoe_s08, "s")
    print("Durchschnittszeit numpy.linalg.qr         :", average_time_numpy_qr, "s")
    print()

    print("=== Laufzeitvergleich fuer zufaellige 100x100-Matrix ===")

    Test = np.random.rand(100, 100)
    A = Test  # wieder Kuengjoe A fuer das timeit-Setup

    t1_random = timeit.repeat(
        "Kuengjoe_S08_Aufg2(A)",
        "from __main__ import Kuengjoe_S08_Aufg2, A",
        number=100,
    )

    t2_random = timeit.repeat(
        "np.linalg.qr(A)",
        "from __main__ import np, A",
        number=100,
    )

    average_time_Kuengjoe_s08_random = np.average(t1_random) / 100.0
    average_time_numpy_qr_random = np.average(t2_random) / 100.0

    print(
        "Durchschnittszeit eigene QR (Kuengjoe_S08_Aufg2) fuer 100x100:",
        average_time_Kuengjoe_s08_random,
        "s",
    )
    print(
        "Durchschnittszeit numpy.linalg.qr fuer 100x100          :",
        average_time_numpy_qr_random,
        "s",
    )
    print()

"""
Kommentar (Kuengjoe):

numpy.linalg.qr ist deutlich schneller, vor allem bei 100x100 Matrizen,
weil es in optimiertem C/FORTRAN läuft und Householder-Verfahren nutzt.
Die eigene Gram-Schmidt-Implementierung ist reines Python und daher
langsamer und numerisch weniger stabil.
"""