def copy_file(source, destination):
    try:
        with open(source, 'r', encoding='utf-8') as src:
            content = src.read()
        with open(destination, 'w', encoding='utf-8') as dest:
            dest.write(content)
        print(f"Файл {source} успешно скопирован в {destination}.")
    except FileNotFoundError:
        print(f"Ошибка: файл {source} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

copy_file("source.txt", "destination.txt")
