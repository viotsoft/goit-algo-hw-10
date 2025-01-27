import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2
def f(x):
    return x**2

# Визначте межі інтегрування, наприклад, від 0 до 2
a = 0  # нижня межа
b = 2  # верхня межа

# Побудова графіка функції
x = np.linspace(a, b, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло для обчислення інтегралу
N = 10000  # Кількість випадкових точок
random_x = np.random.uniform(a, b, N)
random_y = np.random.uniform(0, max(y), N)

under_curve = random_y < f(random_x)
integral_mc = (b - a) * max(y) * np.sum(under_curve) / N

print(f"Значення інтегралу методом Монте-Карло: {integral_mc}")

# Аналітичний метод за допомогою функції quad
result_quad, error = spi.quad(f, a, b)
print(f"Аналітичний метод (quad): {result_quad} з похибкою {error}")

# Порівняння результатів
if np.isclose(integral_mc, result_quad, rtol=1e-2):
    print("Метод Монте-Карло дає результат, близький до аналітичного.")
else:
    print("Метод Монте-Карло не збігається з аналітичним результатом.")