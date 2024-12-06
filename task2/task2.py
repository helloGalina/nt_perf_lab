import math
import sys

def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        x, y = map(float, file.readline().split())
        radius = float(file.readline())
    return x, y, radius

def read_points_data(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            points.append(list(map(float, line.split())))
    return points

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_position(x, y, center_x, center_y, radius):
    distance = calculate_distance(x, y, center_x, center_y)
    if distance < radius:
        return 1
    elif distance == radius:
        return 0
    else:
        return 2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Ошибка: нужно передать два файла как аргументы!")
        sys.exit(1)

    circle_file = sys.argv[1]
    dot_file = sys.argv[2]

    center_x, center_y, radius = read_circle_data(circle_file)
    dots = read_points_data(dot_file)

    for point in dots:
        x, y = point
        result = check_position(x, y, center_x, center_y, radius)
        print(result)
