import threading
import time

def print_numbers():
    for i in range(1, 11):
        print(f"Поток {threading.current_thread().name} выводит число {i}")
        time.sleep(1)

threads = []

for i in range(3):
    thread = threading.Thread(target=print_numbers, name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
