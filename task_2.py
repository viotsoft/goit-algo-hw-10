import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
from scipy.optimize import minimize_scalar

# Визначення функції та меж інтегрування
def f(x):
    return x**2

a = 0
b = 2

# Аналітичний максимум функції на [a, b]
res = minimize_scalar(lambda x: -f(x), bounds=(a, b), method='bounded')
max_f = -res.fun  # Точний максимум

# Генерація точок для графіка
x_plot = np.linspace(a, b, 400)
y_plot = f(x_plot)

# Візуалізація
fig, ax = plt.subplots()
ax.plot(x_plot, y_plot, 'r', linewidth=2)
ax.fill_between(x_plot, y_plot, alpha=0.3)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title(f'Інтегрування f(x) = x² від {a} до {b}')
ax.grid(True)

# Метод Монте-Карло
N = 10000
random_x = np.random.uniform(a, b, N)
random_y = np.random.uniform(0, max_f, N)
under_curve = random_y < f(random_x)

# Візуалізація точок
ax.scatter(random_x[under_curve], random_y[under_curve], color='green', s=1, alpha=0.3, label='Під кривою')
ax.scatter(random_x[~under_curve], random_y[~under_curve], color='red', s=1, alpha=0.3, label='Над кривою')
ax.legend()
plt.show()

# Обчислення інтегралів
integral_mc = (b - a) * max_f * np.mean(under_curve)
result_quad, error_quad = spi.quad(f, a, b)

# Вивід результатів
print(f"Метод Монте-Карло: {integral_mc:.4f}")
print(f"Аналітичний метод: {result_quad:.4f} ± {error_quad:.2e}")

# Порівняння з похибкою
relative_error = abs(integral_mc - result_quad) / result_quad * 100
if relative_error < 1:  # Допустима похибка 1%
    print(f"Результати збігаються (похибка {relative_error:.2f}%).")
else:
    print(f"Похибка завелика: {relative_error:.2f}%!")