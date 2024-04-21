import math
import sys
import io
import time
from memory_profiler import profile

def orientation(p, q, r):
    """
    Функция для определения ориентации тройки точек.
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def distance(p1, p2):
    """Функция для вычисления расстояния между двумя точками."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

@profile
def convex_hull(points):
    """
    Функция для построения выпуклой оболочки множества точек на плоскости.
    Используется алгоритм оболочки Грэхэма.
    """
    start = min(points, key=lambda p: (p[1], p[0]))
    sorted_points = sorted(points, key=lambda p: (math.atan2(p[1]-start[1], p[0]-start[0]), p))
    stack = [start, sorted_points[0]]
    for p in sorted_points[1:]:
        while len(stack) > 1 and orientation(stack[-2], stack[-1], p) != 2:
            stack.pop()
        stack.append(p)
    return stack

def perimeter(convex_hull):
    """Функция для вычисления периметра выпуклой оболочки."""
    perimeter = 0
    for i in range(len(convex_hull)):
        perimeter += distance(convex_hull[i], convex_hull[(i + 1) % len(convex_hull)])
    return perimeter

if __name__ == "__main__":
    # Заменяем стандартный ввод на строку input_data
    input_data = [
        "9\n20 40\n30 40\n30 30\n40 30\n40 40\n50 40\n50 20\n35 20\n20 20\n",
        "5\n2 1\n2 2\n2 3\n3 2\n1 2\n",
        "9\n-2871 6132\n-7251 -7936\n-782 -8113\n1563 5073\n-7688 -9381\n8365 -9630\n5760 -4831\n9068 4835\n-9524 2126\n",
        "6\n-3 6230\n157 7645\n6754 15\n3369 6485\n-9623 -3046\n5139 9127\n",
        "8\n-7573 5625\n-5885 -6754\n6645 602\n9493 2527\n-6672 4034\n-9316 -3445\n-7188 8033\n-2789 4448\n",
        "10\n-9770 7034\n-4413 -6659\n-6803 -551\n6954 -1485\n-9407 -7154\n-5330 -4687\n-5598 436\n7847 9944\n4392 -8106\n7068 3154\n",
        "8\n-6436 -5845\n-4050 4705\n1219 1987\n6274 -1405\n247 -7109\n2770 6536\n49 -3087\n-816 -2067\n",
        "10\n-9419 -8336\n-4425 8012\n6177 -8595\n8820 85\n-6177 -9052\n-4371 8254\n9293 8391\n8772 3642\n-6106 637\n-1674 1798\n",
        "7\n-6635 -2448\n-4870 6477\n-4512 -1031\n-6519 -2628\n258 -1289\n4458 -3083\n-5757 -2813\n",
        "9\n8031 278\n1722 5902\n-2117 7384\n5126 -7896\n-9199 1012\n9212 -1018\n-2877 -1229\n4612 -5241\n2556 -5869\n",
        "7\n-7046 9995\n-6116 -9364\n-5132 896\n-332 304\n9370 2004\n-853 -231\n9456 -4637\n"
    ]
    
    for i, data in enumerate(input_data, start=1):
        sys.stdin = io.StringIO(data)
        
        # Считываем входные данные
        N = int(input())
        points = []
        for _ in range(N):
            x, y = map(int, input().split())
            points.append((x, y))

        # Замеряем время начала выполнения
        start_time = time.time()

        # Выводим номер теста
        print("Тест", i)

        # Строим выпуклую оболочку
        ch = convex_hull(points)

        # Замеряем время окончания выполнения
        end_time = time.time()

        # Вычисляем периметр
        perimeter_value = perimeter(ch)

        # Выводим результат с двумя знаками после запятой
        print("{:.2f}".format(perimeter_value))

        # Выводим затраченное время
        print("Время выполнения: {:.6f} секунд".format(end_time - start_time))
