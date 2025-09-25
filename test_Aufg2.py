from Kuengjoe_S01.Kuengjoe_S01_Aufg2 import _as_1d_array
from Kuengjoe_S01.Kuengjoe_S01_Aufg2 import poly_derivate_coeffs
from Kuengjoe_S01.Kuengjoe_S01_Aufg2 import poly_integrate_coeffs


import numpy as np

def _test_as_1d_array():
    def run_case(name, a):
        try:
            arr = _as_1d_array(a)
            print(f"[OK] {name:22s} -> shape={arr.shape}, ndim={arr.ndim}, dtype={arr.dtype}, values={arr}")
        except Exception as e:
            print(f"[ERRORE] {name:22s} -> {e}")

    print("=== Test _as_1d_array ===")
    run_case("Lista 1D",               [1, 2, 3])
    run_case("Array NumPy 1D",         np.array([1, 2, 3]))
    run_case("Vettore riga 1xN",       np.array([[1, 2, 3]]))
    run_case("Vettore colonna Nx1",    np.array([[1], [2], [3]]))
    run_case("Misto tipi -> float",    [1, 2.5, "3"])    # verrà convertito a float
    run_case("Lista vuota",            [])
    run_case("Matrice 2x2",            np.array([[1, 2], [3, 4]]))
    run_case("Scalare",                5)
    run_case("Tensore 3D",             np.arange(8).reshape(2, 2, 2))

if __name__ == "__main__":
    _test_as_1d_array()
    array = np.array([[2,5,6]])
    arr = _as_1d_array(array)
    print("Input array: "+str(array))
    print("coeff: "+str(arr))
    print("coeff derivate: "+str(poly_derivate_coeffs(arr)))
    print("coeff integrate: "+str(poly_integrate_coeffs(arr)))

    a = np.array([[2, 5, 6]])  # 1x3 -> verrà reso 1D
    a = _as_1d_array(a)
    print("coeff:", a)
    print("coeff derivate:", str(poly_derivate_coeffs(a)))   # atteso [5., 12.]
    print("coeff integrate:", poly_integrate_coeffs(a))