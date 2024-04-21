# №1
def symmetric_difference(set_a, set_b):
    result = []
    i, j = 0, 0
    
    while i < len(set_a) and j < len(set_b):
        if set_a[i] < set_b[j]:
            result.append(set_a[i])
            i += 1
        elif set_a[i] > set_b[j]:
            result.append(set_b[j])
            j += 1
        else:
            i += 1
            j += 1
    
    while i < len(set_a):
        result.append(set_a[i])
        i += 1
    
    while j < len(set_b):
        result.append(set_b[j])
        j += 1
    
    return result

if __name__ == "__main__":
    set_a = set()
    set_b = set()

    # Считываем множества А и В
    current_set = set_a
    for num in map(int, input().split()):
        if num == 0:
            current_set = set_b
            continue
        current_set.add(num)

    # Вычисляем симметрическую разность
    result = sorted(set_a.symmetric_difference(set_b))
    
    if result:
        print(' '.join(map(str, result)))
    else:
        print(0)


        