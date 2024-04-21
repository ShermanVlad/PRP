import math

def f(x):
    return math.exp(x) + 4 * math.sin(x) - x

def df(x):
    return math.exp(x) + 4 * math.cos(x) - 1

def newton_method(x0, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        fx = f(x0)
        if abs(fx) < tol:
            return x0
        x0 -= fx / df(x0)
    return None

def bisection_method(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        return None
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol:
            return c
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return None

# Використання методу Ньютона
x0 = 0  # Початкове наближення
solution_newton = newton_method(x0)
print("Розв'язок за допомогою методу Ньютона:", solution_newton)

# Використання методу бісекції
a = -1
b = 1
solution_bisection = bisection_method(a, b)
print("Розв'язок за допомогою методу бісекції:", solution_bisection)
