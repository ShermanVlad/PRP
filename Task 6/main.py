import numpy as np
import matplotlib.pyplot as plt

# Визначення функцій
def f1(x, y):
    return np.sin(x + 2) - y - 1.5

def f2(x, y):
    return x + np.cos(y - 2) - 0.5

# Створення сітки точок для області, де будемо шукати перетини
x_values = np.linspace(-5, 5, 400)
y_values = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x_values, y_values)

# Розрахунок значень функцій на сітці точок
Z1 = f1(X, Y)
Z2 = f2(X, Y)

# Побудова графіків
plt.figure(figsize=(10, 6))
plt.contour(X, Y, Z1, levels=[0], colors='r')
plt.contour(X, Y, Z2, levels=[0], colors='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графіки функцій')
plt.text(2, 2, 'sin(x+2) - y - 1.5 = 0', color='red')
plt.text(2, 3, 'x + cos(y-2) - 0.5 = 0', color='blue')
plt.grid(True)
plt.show()
