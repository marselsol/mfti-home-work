def runge_kutta_4(f, x0, y0, h, x_end):
    x, y = x0, y0
    while x < x_end:
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h / 2 * k1)
        k3 = f(x + h / 2, y + h / 2 * k2)
        k4 = f(x + h, y + h * k3)
        y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
    return y


f = lambda x, y: 2 * x  # y' = 2x
x0, y0 = 0, 1
h = 0.1
x_end = 1

# Численное решение методом Рунге-Кутты 4-го порядка
y_rk = runge_kutta_4(f, x0, y0, h, x_end)

# Аналитическое решение
y_exact = x_end ** 2 + 1

# Вывод результатов
print(f"Численное решение методом Рунге-Кутты: y({x_end}) = {y_rk}")
print(f"Аналитическое решение: y({x_end}) = {y_exact}")
print(f"Погрешность: {abs(y_rk - y_exact)}")
