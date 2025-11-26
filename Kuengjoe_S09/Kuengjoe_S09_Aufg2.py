import numpy as np


def Kuengjoe_S09_Aufg2(A: np.ndarray, A_tilde: np.ndarray,
                   b: np.ndarray, b_tilde: np.ndarray):
    try:
        x = np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        raise ValueError(f"Ungestörte Matrix A ist singulär oder schlecht konditioniert: {e}")

    try:
        x_tilde = np.linalg.solve(A_tilde, b_tilde)
    except np.linalg.LinAlgError as e:
        raise ValueError(f"Gestörte Matrix A_tilde ist singulär oder schlecht konditioniert: {e}")

    norm_A_inf = np.linalg.norm(A, np.inf)
    norm_AtAtilde = np.linalg.norm(A - A_tilde, np.inf)
    norm_b_inf = np.linalg.norm(b, np.inf)
    norm_bbtilde = np.linalg.norm(b - b_tilde, np.inf)

    cond_A_inf = np.linalg.cond(A, np.inf)

    ratio_A = norm_AtAtilde / norm_A_inf
    ratio_b = norm_bbtilde / norm_b_inf

    if cond_A_inf * ratio_A < 1.0:
        dx_max = (cond_A_inf / (1 - cond_A_inf * ratio_A)) \
                 * (ratio_A + ratio_b)
    else:
        dx_max = np.nan

    # 4. Beobachteter Fehler
    dx_obs = np.linalg.norm(x - x_tilde, np.inf) / np.linalg.norm(x, np.inf)

    return x, x_tilde, dx_max, dx_obs


if __name__ == "__main__":
    A = np.array([[1, 0, 2],
                  [0, 1, 0],
                  [1e-4, 0, 1e-4]])
    At = A.copy()
    At[0, 2] += 1e-6
    b = np.array([1, 1, 0])
    bt = b.copy();
    bt[2] += 1e-7

    x, xt, dx_max, dx_obs = Kuengjoe_S09_Aufg2(A, At, b, bt)
    print("dx_obs =", dx_obs, "   dx_max =", dx_max)
