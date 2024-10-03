def get_list_element():
    my_list = [10, 20, 30, 40, 50]
    try:
        index = int(input("Введите индекс элемента списка: "))
        print(f"Элемент по индексу {index}: {my_list[index]}")
    except IndexError:
        print("Ошибка: индекс выходит за пределы списка!")
    except ValueError:
        print("Ошибка: введено не число!")

get_list_element()
