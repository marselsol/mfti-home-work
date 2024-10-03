class EvenNumberException(Exception):
    pass

class NegativeNumberException(Exception):
    pass

def sum_list_elements(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            raise EvenNumberException(f"Найдено четное число: {num}")
        if num < 0:
            raise NegativeNumberException(f"Найдено отрицательное число: {num}")
        total += num
    return total

try:
    my_list = [1, 3, -5, 7]
    print(f"Сумма списка: {sum_list_elements(my_list)}")
except EvenNumberException as e:
    print(e)
except NegativeNumberException as e:
    print(e)
