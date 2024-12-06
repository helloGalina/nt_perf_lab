n = int(input("Введите размер массива n: "))
m = int(input("Введите шаг m: "))

arr = [str(i) for i in range(1, n+1)]

index = 0
path = []

for _ in range(n):
    index = (index + m - 1) % len(arr)  # Найти индекс для удаления
    path.append(arr.pop(index))

print("Путь:", "".join(path))
