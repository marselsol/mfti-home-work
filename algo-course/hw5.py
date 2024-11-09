def reverse_characters_in_words(s):
    return ' '.join(word[::-1] for word in s.split())

while True:
    input_string = input("Введите строку (или 'выход' для завершения): ")
    if input_string.lower() == 'выход' or not input_string.strip():
        print("Программа завершена.")
        break
    result = reverse_characters_in_words(input_string)
    print("Результат:", result)
