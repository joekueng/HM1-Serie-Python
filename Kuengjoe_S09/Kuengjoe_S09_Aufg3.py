

import numpy as np
import matplotlib.pyplot as plt

try:
    from Kuengjoe_S09_Aufg2 import Kuengjoe_S09_Aufg2
except ImportError as exc:
    raise RuntimeError(
        "Fehler: Die Datei Kuengjoe_S09_Aufg2.py konnte nicht importiert werden.\n"
        "Stellen Sie sicher, dass sie im selben Verzeichnis liegt."
    ) from exc


def main():
    n_iter = 1000
    size   = 100

    dx_max_vec = np.empty(n_iter)
    dx_obs_vec = np.empty(n_iter)
    ratio_vec  = np.empty(n_iter)

    for i in range(n_iter):
        A = np.random.rand(size, size)
        b = np.random.rand(size)

        A_tilde = A + np.random.rand(size, size) / 10**5
        b_tilde = b + np.random.rand(size)       / 10**5

        x, x_tilde, dx_max, dx_obs = Kuengjoe_S09_Aufg2(A, A_tilde, b, b_tilde)

        dx_max_vec[i] = dx_max
        dx_obs_vec[i] = dx_obs

        if np.isfinite(dx_max) and dx_obs > 0:
            ratio_vec[i] = dx_max / dx_obs
        else:
            ratio_vec[i] = np.nan


    plt.figure(figsize=(10, 6))
    idx = np.arange(n_iter)
    mask_dxmax = np.isfinite(dx_max_vec)
    mask_dxobs = np.isfinite(dx_obs_vec)

    plt.semilogy(idx[mask_dxmax], dx_max_vec[mask_dxmax],
                 label='dx_max', linewidth=1.2, alpha=0.8)
    plt.semilogy(idx[mask_dxobs], dx_obs_vec[mask_dxobs],
                 label='dx_obs', linewidth=1.2, alpha=0.8)
    plt.semilogy(idx[~np.isnan(ratio_vec)], ratio_vec[~np.isnan(ratio_vec)],
                 label='dx_max / dx_obs', linewidth=1.2, alpha=0.8)

    plt.xlabel('Iteration')
    plt.ylabel(r'Relative Fehler (∞‑Norm)')
    plt.title('dx_max, dx_obs und ihr Verhältnis über 1000 zufällige Tests')
    plt.legend()
    plt.grid(True, which='both', ls='--', lw=0.5)
    plt.tight_layout()
    plt.show()


    finite_mask = np.isfinite(ratio_vec)
    mean_ratio  = np.nanmean(ratio_vec[finite_mask])
    print(f"\nDurchschnittliches Verhältnis dx_max/dx_obs (nur finite Werte): {mean_ratio:.2f}")

    print("\nKommentar:")
    print("dx_max usually exceeds dx_obs by 10–1000×; occasional NaNs occur when "
          "cond(A)*||A−A_tilde||/||A||≥1, shown as gaps.")


if __name__ == "__main__":
    main()
