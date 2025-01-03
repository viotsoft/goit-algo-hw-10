import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
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

# Аналітичне обчислення інтегралу

integral_analytical, _ = quad(f, a, b)
print(f"Аналітичне значення інтегралу: {integral_analytical}")

# Висновки
error = abs(integral_mc - integral_analytical)
print(f"Похибка методу Монте-Карло: {error}")
# Перевірка результатів
if np.isclose(integral_mc, integral_analytical, rtol=1e-2):
    print("Метод Монте-Карло дає результат, близький до аналітичного.")
else:
    print("Метод Монте-Карло не збігається з аналітичним результатом.")

    import scipy.integrate as spi

    # Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2
    def f(x):
        return x**2

    # Визначте межі інтегрування, наприклад, від 0 до 1
    a = 0  # нижня межа
    b = 2  # верхня межа

    # Обчислення інтеграла
    result, error = spi.quad(f, a, b)

    print("Інтеграл: ", result, error)

    