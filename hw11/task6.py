def calculate_square_root():
    try:
        import math
        number = float(input("Введите число для вычисления квадратного корня: "))
        if number < 0:
            raise ValueError("Ошибка: нельзя вычислить квадратный корень отрицательного числа!")
        print(f"Квадратный корень: {math.sqrt(number)}")
    except ImportError:
        print("Ошибка: не удалось импортировать модуль math!")
    except ValueError as e:
        print(e)

calculate_square_root()
