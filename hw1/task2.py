def divide_numbers():
    try:
        numerator = float(input("Введите числитель: "))
        denominator = float(input("Введите знаменатель: "))
        result = numerator / denominator
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    except ValueError:
        print("Ошибка: введено не число!")
    else:
        print(f"Результат: {result}")

divide_numbers()
