def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        words = content.split()
        print(f"Количество слов в файле: {len(words)}")
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

count_words("text_file.txt")
