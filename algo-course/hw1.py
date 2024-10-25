def sum_of_four_numbers():
    numbers = []
    for i in range(4):
        num = float(input(f"Введите число {i + 1}: "))
        numbers.append(num)

    total_sum = sum(numbers)

    print(f"Сумма введенных чисел: {total_sum}")


print("Первый набор данных:")
sum_of_four_numbers()

print("\nВторой набор данных:")
sum_of_four_numbers()