import numpy as np
import matplotlib.pyplot as plt

# Визначення функцій системи рівнянь
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

# Побудова графіків функцій
plt.figure(figsize=(10, 6))
plt.contour(X, Y, Z1, levels=[0], colors='r')
plt.contour(X, Y, Z2, levels=[0], colors='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графіки функцій системи рівнянь')
plt.grid(True)
plt.show()

# Пошук перетину графіків для знаходження початкового наближення
# У нашому випадку, візьмемо центральну точку області
x0 = 0
y0 = 0

# Визначення функцій системи рівнянь
def F(x, y):
    return np.array([f1(x, y), f2(x, y)])

def J(x, y):
    return np.array([
        [np.cos(x + 2), -1],
        [1, np.sin(y - 2)]
    ])

# Метод Ньютона
def newton_method(x0, y0, max_iter=100, tol=1e-6):
    x_prev, y_prev = x0, y0
    for i in range(max_iter):
        delta = np.linalg.solve(J(x_prev, y_prev), -F(x_prev, y_prev))
        x_next, y_next = x_prev + delta[0], y_prev + delta[1]
        if np.linalg.norm(delta) < tol:
            return x_next, y_next, i + 1
        x_prev, y_prev = x_next, y_next
    return x_prev, y_prev, max_iter

# Виклик методів для обчислення коренів системи рівнянь
x_newton, y_newton, num_iter_newton = newton_method(x0, y0)

# Виведення результатів

print("\nМетод Ньютона:")
print(f"Корені системи рівнянь: x = {x_newton}, y = {y_newton}")
print(f"Кількість ітерацій: {num_iter_newton}")
