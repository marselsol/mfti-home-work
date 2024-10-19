import threading

def calculate_squares():
    for i in range(1, 11):
        print(f"Квадрат числа {i} равен {i ** 2}")

def calculate_cubes():
    for i in range(1, 11):
        print(f"Куб числа {i} равен {i ** 3}")

if __name__ == "__main__":
    thread1 = threading.Thread(target=calculate_squares)
    thread2 = threading.Thread(target=calculate_cubes)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
