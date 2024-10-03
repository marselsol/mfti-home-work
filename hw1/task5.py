def convert_to_float():
    try:
        user_input = input("Введите строку для преобразования в число с плавающей точкой: ")
        float_value = float(user_input)
        print(f"Преобразованное значение: {float_value}")
    except ValueError:
        print("Ошибка: невозможно преобразовать строку в число с плавающей точкой!")

convert_to_float()
