import numpy as np
import matplotlib.pyplot as plt

original_years = np.array([1997, 1999, 2006, 2010], dtype=float)
number_of_days_with_extreme_uv = np.array([150, 104, 172, 152], dtype=float)


reference_year = original_years[0]
shifted_years = original_years - reference_year

vandermonde_matrix = np.vander(shifted_years, 4)
coefficients = np.linalg.solve(vandermonde_matrix, number_of_days_with_extreme_uv)

fine_grind_shifted_years = np.linspace(0, shifted_years[-1], 400)
fine_grind_original_years = fine_grind_shifted_years + reference_year

polynomial_coefficients = np.polynomial.Polynomial(coefficients[::-1])

estimate_2003 = polynomial_coefficients(2003 - reference_year)
estimate_2004 = polynomial_coefficients(2004 - reference_year)

polynomial_coefficients_polyfit = np.polyfit(shifted_years, number_of_days_with_extreme_uv, 3)
polynomial_values_polyfit = np.polyval(polynomial_coefficients_polyfit, fine_grind_shifted_years)

estimate_2003_polyfit = np.polyval(polynomial_coefficients_polyfit, 2003 - reference_year)
estimate_2004_polyfit = np.polyval(polynomial_coefficients_polyfit, 2004 - reference_year)

plt.figure()
plt.plot(original_years, number_of_days_with_extreme_uv, 'o', label='Datenpunkte', markersize=8)
plt.plot(fine_grind_original_years, polynomial_coefficients(fine_grind_shifted_years), label='Eigenes Polynom', linewidth=2)
plt.plot(fine_grind_original_years, polynomial_values_polyfit, label='NumPy polyfit', linestyle='--', linewidth=2)
plt.xlabel('Jahr')
plt.ylabel('Anzahl Tage mit extrem UV-Strahlung')
plt.title('Interpolation der Anzahl Tage mit extrem UV-Strahlung')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("coefficients (eigenes Polynom):", coefficients)
print("coefficients (NumPy polyfit):", polynomial_coefficients_polyfit)
print(f"Schätzung für 2003 (eigenes Polynom): {estimate_2003:.2f}")
print(f"Schätzung für 2004 (eigenes Polynom): {estimate_2004:.2f}")
print(f"Schätzung für 2003 (NumPy polyfit): {estimate_2003_polyfit:.2f}")
print(f"Schätzung für 2004 (NumPy polyfit): {estimate_2004_polyfit:.2f}")

