# Функція для обчислення наступного наближення за методом простих ітерацій
def simple_iteration_method(x1, x2, x3):
    new_x1 = (7 - x2 - x3) / 5
    new_x2 = (5 - 3*x1 - x3) / -3
    new_x3 = (2 - 2*x1 - 6*x2) / 3
    return new_x1, new_x2, new_x3

# Функція для обчислення наступного наближення за методом Гауса-Зейделя
def gauss_seidel_method(x1, x2, x3):
    new_x1 = (7 - x2 - x3) / 5
    new_x2 = (5 - 3*new_x1 - x3) / -3
    new_x3 = (2 - 2*new_x1 - 6*new_x2) / 3
    return new_x1, new_x2, new_x3

# Початкові значення
x1, x2, x3 = 0, 0, 0

# Точність
epsilon = 1e-6

# Максимальна кількість ітерацій
max_iterations = 1000

# Ітерації методу простих ітерацій
for i in range(max_iterations):
    new_x1, new_x2, new_x3 = simple_iteration_method(x1, x2, x3)
    if abs(new_x1 - x1) < epsilon and abs(new_x2 - x2) < epsilon and abs(new_x3 - x3) < epsilon:
        print("Метод простих ітерацій: збіг до розв'язку з точністю до ", epsilon)
        print("Розв'язок: x1 =", new_x1, "x2 =", new_x2, "x3 =", new_x3)
        break
    x1, x2, x3 = new_x1, new_x2, new_x3
else:
    print("Метод простих ітерацій не зійшовся за ", max_iterations, "ітерацій")

# Початкові значення
x1, x2, x3 = 0, 0, 0

# Ітерації методу Гауса-Зейделя
for i in range(max_iterations):
    new_x1, new_x2, new_x3 = gauss_seidel_method(x1, x2, x3)
    if abs(new_x1 - x1) < epsilon and abs(new_x2 - x2) < epsilon and abs(new_x3 - x3) < epsilon:
        print("Метод Гауса-Зейделя: збіг до розв'язку з точністю до ", epsilon)
        print("Розв'язок: x1 =", new_x1, "x2 =", new_x2, "x3 =", new_x3)
        break
    x1, x2, x3 = new_x1, new_x2, new_x3
else:
    print("Метод Гауса-Зейделя не зійшовся за ", max_iterations, "ітерацій")
