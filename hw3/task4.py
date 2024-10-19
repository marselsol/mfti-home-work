from multiprocessing import Process

def compute_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Факториал числа {n} равен {result}")

if __name__ == "__main__":
    processes = []

    for i in range(1, 11):
        process = Process(target=compute_factorial, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
