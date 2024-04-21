def check_dangerous_menu(menu, dangerous):
    for product in menu:
        if product in dangerous:
            return "NO"
    return "YES"

def main():
    # Чтение данных
    N = int(input())  # Количество продуктов в меню
    menu = [input() for _ in range(N)]  # Список продуктов в меню
    K = int(input())  # Количество студентов
    dangerous_menus = []  # Список опасных продуктов для каждого студента
    for _ in range(K + 1):
        Ni = int(input())  # Количество опасных продуктов
        dangerous_menus.append(set(input() for _ in range(Ni)))  # Опасные продукты для текущего студента
    M = int(input())  # Количество продуктов в раздаче

    # Проверка безопасности обеда для каждого студента
    for i in range(K):
        result = check_dangerous_menu(menu, dangerous_menus[i])
        print(result)

if __name__ == "__main__":
    main()