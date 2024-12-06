import sys

# Функция для подсчёта минимальных ходов
def min_moves(nums):
    nums.sort()  # Сортируем список
    median = nums[len(nums) // 2]  # Находим медиану
    moves = 0
    for num in nums:
        moves += abs(num - median)  # Считаем разницу
    return moves

if __name__ == "__main__":
    # Проверяем, передан ли путь к файлу
    if len(sys.argv) != 2:
        print("Ошибка: укажите путь к файлу с числами!")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        # Читаем числа из файла
        with open(file_path, 'r') as file:
            nums = []
            for line in file:
                nums.append(int(line.strip()))

        # Выводим результат
        print("Минимальное количество ходов:", min_moves(nums))
    except Exception as e:
        print("Ошибка при обработке файла:", e)
