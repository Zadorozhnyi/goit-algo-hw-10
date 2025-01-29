import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a, b = 0, 2  # Межі інтегрування
num_samples = 100000  # Кількість випадкових точок

# Метод Монте-Карло для визначеного інтегралу
x_rand = np.random.uniform(a, b, num_samples)
y_rand = np.random.uniform(0, f(b), num_samples)

under_curve = y_rand <= f(x_rand)
monte_carlo_result = (b - a) * f(b) * np.mean(under_curve)

# Обчислення інтеграла за допомогою функції quad
quad_result, error = spi.quad(f, a, b)

# Візуалізація методу Монте-Карло
x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'r', linewidth=2, label="f(x) = x^2")
plt.fill_between(x, y, alpha=0.3, color='gray', label="Область під кривою")
plt.scatter(x_rand, y_rand, c=under_curve, cmap='coolwarm', s=0.5, alpha=0.5)
plt.axvline(x=a, color='gray', linestyle='--')
plt.axvline(x=b, color='gray', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Метод Монте-Карло для обчислення інтегралу')
plt.legend()
plt.grid()
plt.show()

# Вивід результатів
print(f"Метод Монте-Карло: {monte_carlo_result:.6f}")
print(f"Функція quad: {quad_result:.6f} (похибка: {error:.6e})")
