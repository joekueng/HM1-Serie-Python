def Kuengjoe_S06_Aufg2(A, b, eps=1e-12):

    lenA = len(A)
    A_work = [row[:] for row in A]
    b_work = b[:]


    if any(len(row) != lenA for row in A_work):
        raise ValueError("A muss eine quadratische Matrix sein")
    if len(b_work) != lenA:
        raise ValueError("Länge von b muss mit der Anzahl der Zeilen von A übereinstimmen")

    det_sign = 1


    for k in range(lenA):
        pivot_row = max(range(k, lenA), key=lambda i: abs(A_work[i][k]))
        pivot = A_work[pivot_row][k]

        if abs(pivot) < eps:
            raise ValueError("Matrice singolare während der Pivotisierung")

        if pivot_row != k:
            A_work[k], A_work[pivot_row] = A_work[pivot_row], A_work[k]
            b_work[k], b_work[pivot_row] = b_work[pivot_row], b_work[k]
            det_sign *= -1

        for i in range(k + 1, lenA):
            factor = A_work[i][k] / A_work[k][k]
            A_work[i][k] = 0.0
            for j in range(k + 1, lenA):
                A_work[i][j] -= factor * A_work[k][j]
            b_work[i] -= factor * b_work[k]

    detA = det_sign
    for i in range(lenA):
        detA *= A_work[i][i]

    solution = [0.0] * lenA
    for i in reversed(range(lenA)):
        if abs(A_work[i][i]) < eps:
            raise ValueError("Matrice singolare während der Rückwärtseinsetzung")
        summ = sum(A_work[i][j] * solution[j] for j in range(i + 1, lenA))
        solution[i] = (b_work[i] - summ) / A_work[i][i]

    A_triangle = A_work
    return A_triangle, detA, solution


if __name__ == "__main__":
    coefficient_matrix_A1 = [
        [4, -1, -5],
        [-12, 4, 17],
        [32, -10, -41],
    ]
    rhs_A1_primary = [-5, 19, -39]
    rhs_A1_secondary = [6, -12, 48]

    coefficient_matrix_A2 = [
        [2, 7, 3],
        [-4, -10, 0],
        [12, 34, 9],
    ]
    rhs_A2_primary = [25, -24, 107]
    rhs_A2_secondary = [5, -22, 42]

    coefficient_matrix_A3 = [
        [-2, 5, 4],
        [-14, 38, 22],
        [6, -9, -27],
    ]
    rhs_A3_primary = [1, 40, 75]
    rhs_A3_secondary = [16, 82, -120]

    coefficient_matrix_A4 = [
        [-1, 2, 3, 2, 5, 4, 3, -1],
        [3, 4, 2, 1, 0, 2, 3, 8],
        [2, 7, 5, -1, 2, 1, 3, 5],
        [3, 1, 2, 6, -3, 7, 2, -2],
        [5, 2, 0, 8, 7, 6, 1, 3],
        [-1, 3, 2, 3, 5, 3, 1, 4],
        [8, 7, 3, 6, 4, 9, 7, 9],
        [-3, 14, -2, 1, 0, -2, 10, 5],
    ]
    rhs_A4 = [-11, 103, 53, -20, 95, 78, 131, -26]
    A = [
        [2.0, -1.0, 1.0],
        [3.0,  3.0, 9.0],
        [3.0,  3.0, 5.0],
    ]
    b = [2.0, -1.0, 4.0]
    U, detA, x = Kuengjoe_S06_Aufg2(A, b)
    print("U =", U)
    print("det(A) =", detA)
    print("x =", x)

    linear_systems_to_solve = [
        ("A1_primary", coefficient_matrix_A1, rhs_A1_primary),
        ("A1_secondary", coefficient_matrix_A1, rhs_A1_secondary),
        ("A2_primary", coefficient_matrix_A2, rhs_A2_primary),
        ("A2_secondary", coefficient_matrix_A2, rhs_A2_secondary),
        ("A3_primary", coefficient_matrix_A3, rhs_A3_primary),
        ("A3_secondary", coefficient_matrix_A3, rhs_A3_secondary),
        ("A4", coefficient_matrix_A4, rhs_A4),
    ]

    for system_label, matrix_A, vector_b in linear_systems_to_solve:
        upper_triangular_matrix_U, determinant_of_A, solution_vector_x = Kuengjoe_S06_Aufg2(
            [row[:] for row in matrix_A],   # copia profonda – preserva i dati originali
            vector_b[:]                     # idem per il termine noto
        )
        print(f"{system_label}:")
        print("  U       =", upper_triangular_matrix_U)
        print("  det(A)  =", determinant_of_A)
        print("  x       =", solution_vector_x)
        print()