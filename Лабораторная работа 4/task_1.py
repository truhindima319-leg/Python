Импортный CSV
Импорт JSON

INPUT_FILENAME = «input.csv»
OUTPUT_FILENAME = «output.json»


def task() -> Нет:
    ...  # TODO считать содержимое csv файла
 с open(INPUT_FILENAME, 'r', кодирование='utf-8') как f:
 data = list(csv. DictReader(f))
    ...  # TODO Сериализовать в файл с отступами равными 4
 с open(OUTPUT_FILENAME, 'w', кодирование='utf-8') как f:
 json.dump(data, f, ensure_ascii=Ложно, отступ=4)

если __name__ == '__main__':
    # Нужно для проверки
 задача()

 с open(OUTPUT_FILENAME) как output_f:
 для строки в output_f:
            print(line, end="")
