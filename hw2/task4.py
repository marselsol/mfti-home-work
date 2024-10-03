def copy_unique_lines(input_file, output_file):
    unique_lines = set()
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                unique_lines.add(line.strip())

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in unique_lines:
                outfile.write(line + '\n')
        print(f"Уникальные строки из {input_file} успешно записаны в {output_file}.")
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

copy_unique_lines("input.txt", "unique_output.txt")
