import time
import io
import sys
from memory_profiler import profile

def symmetric_difference(set_a, set_b):
    result = sorted(set_a.symmetric_difference(set_b))
    return result if result else [0]

# Функция для запуска теста
@profile
def run_test(input_data):
    # Заменяем стандартный ввод на строку input_data
    sys.stdin = io.StringIO(input_data)

    # Запускаем программу
    set_a = set()
    set_b = set()
    current_set = set_a
    for num in map(int, input().split()):
        if num == 0:
            current_set = set_b
            continue
        current_set.add(num)
    return symmetric_difference(set_a, set_b)

# Тестовые данные
test_data = [
    ("1 2 3 4 5 0 1 7 5 8 0\n", [2, 3, 4, 7, 8]),
    ("1 2 6 8 7 3 0 4 1 6 2 6 2 3 9 0\n", [4, 7, 8, 9]),
    ("10 35 30 0 15 25 1 5 10\n", [1, 5, 15, 25, 30, 35]),
    ("5 4 3 2 1 0 9 8 7 6 0\n", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ("600 200 300 400 0 500 600 20000 0\n", [200, 300, 400, 500, 20000]),
    ("2 4 6 8 0 1 3 5 7 9 0\n", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ("111 222 444 0 444 555 666 0\n", [111, 222, 555, 666]),
    ("123 234 345 456 0 567 678 789 0\n", [123, 234, 345, 456, 567, 678, 789]),
    ("23 34 45 56 67 0 78 34 90 0\n", [23, 45, 56, 67, 78, 90]),
    ("1 1 1 1 1 0 2 2 2 2\n", [1, 2]),
    ("543 654 765 0 876 987 0\n", [543, 654, 765, 876, 987]),
    # Добавьте здесь еще тестовые наборы данных
]

# Запуск тестов и вывод результатов
for i, (input_data, expected_output) in enumerate(test_data, 1):
    # Измеряем время начала выполнения
    start_time = time.perf_counter()

    # Запускаем тест
    result = run_test(input_data)

    # Измеряем время окончания выполнения
    end_time = time.perf_counter()

    # Выводим результаты теста
    print(f"Тест {i}:")
    print(f"Ожидаемый результат: {expected_output}")
    print(f"Фактический результат: {result}")
    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print()
