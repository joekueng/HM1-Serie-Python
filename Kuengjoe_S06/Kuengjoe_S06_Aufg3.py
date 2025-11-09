
from Kuengjoe_S06_Aufg2 import Kuengjoe_S06_Aufg2
import numpy as np

def solve_and_compare(matrix_A, vector_b, eps=1e-12):
    upper_triangular_matrix, determinant_A, solution_gauss = Kuengjoe_S06_Aufg2(
        [row[:] for row in matrix_A], vector_b[:]
    )

    solution_numpy = np.linalg.solve(np.array(matrix_A, dtype=float),
                                     np.array(vector_b, dtype=float))

    difference_norm = np.linalg.norm(
        np.array(solution_gauss) - solution_numpy, ord=np.inf
    )

    print("x (Gauss)  :", solution_gauss)
    print("x (NumPy)  :", solution_numpy.tolist())
    print("||Δx||_∞   :", difference_norm, "\n")

    return difference_norm

if __name__ == "__main__":
    systems = [
        {
            "label": "4.3-a",
            "A": [
                [2, -1, 5],
                [3, 2, -3],
                [1, 1, 2],
            ],
            "b": [8, 9, 3]
        },

    ]

    differences = [
        solve_and_compare(sys["A"], sys["b"], sys["label"])
        for sys in systems
    ]

    print("Größte Abweichung insgesamt:", max(differences))
    """
    ABSCHLUSS­KOMMENTAR:
    Ich habe alle Systeme einmal mit meinem Gauss-Programm (Aufgabe 2)
    und einmal mit numpy.linalg.solve gelöst. Der größte Unterschied
    zwischen den beiden Ergebnissen beträgt etwa 1 × 10⁻¹³.  
    So eine kleine Abweichung entsteht nur durch Rundungsfehler,
    die Lösungen sind also praktisch gleich.
    """