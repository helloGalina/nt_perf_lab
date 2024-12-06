import json
import sys
import os

def load_file(file_path):
    """Читает JSON-файл и возвращает данные."""
    with open(file_path, 'r') as file:
        return json.load(file)

def save_file(file_path, data):
    """Сохраняет данные в JSON-файл."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def update_values(tests, values_dict):
    """Рекурсивно заполняет поле 'value' в тестах."""
    for test in tests:
        test_id = test.get("id")
        if test_id in values_dict:
            test["value"] = values_dict[test_id]
        if "values" in test:  # Если есть вложенные тесты
            update_values(test["values"], values_dict)

if __name__ == "__main__":
    # Проверяем количество аргументов
    if len(sys.argv) != 4:
        print("Ошибка: укажите пути к файлам tests.json, values.json и report.json!")
        sys.exit(1)

    # Получаем пути к файлам
    tests_path = sys.argv[1]
    values_path = sys.argv[2]
    report_path = sys.argv[3]

    # Загружаем данные из файлов
    tests_data = load_file(tests_path)
    values_data = load_file(values_path)

    # Создаем словарь для значений
    values_dict = {item["id"]: item["value"] for item in values_data["values"]}

    # Обновляем значения в тестах
    update_values(tests_data["tests"], values_dict)

    # Сохраняем результат
    save_file(report_path, tests_data)

    print(f"Отчет успешно сохранен в файл: {report_path}")
