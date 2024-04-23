import numpy as np

def g(x, y):
    return 1.5 + np.sin(x + 2)

def h(x, y):
    return 0.5 - np.cos(y - 2)

def simple_iteration_method(x0, y0, max_iter=100, tol=1e-6):
    x_prev, y_prev = x0, y0
    for i in range(max_iter):
        x_next = g(x_prev, y_prev)
        y_next = h(x_prev, y_prev)
        if np.abs(x_next - x_prev) < tol and np.abs(y_next - y_prev) < tol:
            return x_next, y_next, i + 1
        x_prev, y_prev = x_next, y_next
    return x_prev, y_prev, max_iter

# Початкове наближення, взяте з графіку
x0, y0 = -1.5, 2.0
# Максимальна кількість ітерацій і точність
max_iter = 100
tolerance = 1e-6

# Виклик методу простих ітерацій
x_si, y_si, num_iter_si = simple_iteration_method(x0, y0, max_iter, tolerance)

print("Метод простих ітерацій:")
print(f"Корені системи рівнянь: x = {x_si}, y = {y_si}")
print(f"Кількість ітерацій: {num_iter_si}")

