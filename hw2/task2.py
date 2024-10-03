def calculate_total_cost(filename):
    total_cost = 0
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, quantity, price = line.strip().split(',')
                    total_cost += int(quantity) * float(price)
                except ValueError:
                    print(f"Ошибка в формате строки: {line}")
        print(f"Общая стоимость заказа: {total_cost} рублей.")
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

calculate_total_cost("prices.txt")
