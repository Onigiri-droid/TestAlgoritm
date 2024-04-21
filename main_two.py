import math

def orientation(p, q, r):
    """
    Функция для определения ориентации тройки точек.
    Возвращает:
    - 0, если точки коллинеарны
    - 1, если точки образуют положительный поворот (против часовой стрелки)
    - 2, если точки образуют отрицательный поворот (по часовой стрелке)
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Коллинеарные
    return 1 if val > 0 else 2  # Положительный или отрицательный поворот

def distance(p1, p2):
    """Функция для вычисления расстояния между двумя точками."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def convex_hull(points):
    """
    Функция для построения выпуклой оболочки множества точек на плоскости.
    Используется алгоритм оболочки Грэхэма.
    """
    # Находим самую левую нижнюю точку
    start = min(points, key=lambda p: (p[1], p[0]))

    # Сортируем остальные точки по полярному углу относительно начальной точки
    sorted_points = sorted(points, key=lambda p: (math.atan2(p[1]-start[1], p[0]-start[0]), p))

    # Инициализируем стек для построения оболочки
    stack = [start, sorted_points[0]]

    # Построение оболочки
    for p in sorted_points[1:]:
        while len(stack) > 1 and orientation(stack[-2], stack[-1], p) != 2:
            stack.pop()
        stack.append(p)

    return stack

def perimeter(convex_hull):
    """
    Функция для вычисления периметра выпуклой оболочки.
    """
    perimeter = 0
    for i in range(len(convex_hull)):
        perimeter += distance(convex_hull[i], convex_hull[(i + 1) % len(convex_hull)])
    return perimeter

# Считываем входные данные
N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# Строим выпуклую оболочку
ch = convex_hull(points)

# Вычисляем периметр
perimeter = perimeter(ch)

# Выводим результат с двумя знаками после запятой
print("{:.2f}".format(perimeter))
