def sum_negatives_between_max_min(arr):
    """
    Возвращает сумму отрицательных элементов,
    расположенных между максимальным и минимальным элементами массива.
    """
    if not arr:
        return 0

    # Индексы первого максимума и первого минимума
    max_idx = 0
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
        if arr[i] < arr[min_idx]:
            min_idx = i

    # Границы отрезка "между"
    left = min(max_idx, min_idx)
    right = max(max_idx, min_idx)

    # Суммируем отрицательные элементы строго между границами
    total = 0
    for i in range(left + 1, right):
        if arr[i] < 0:
            total += arr[i]

    return total


def main():
    # Пример ввода
    n = int(input("Введите размер массива N: "))
    print(f"Введите {n} элементов через пробел:")
    arr = list(map(int, input().split()))

    if len(arr) != n:
        print("Ошибка: количество введённых элементов не совпадает с N")
        return

    result = sum_negatives_between_max_min(arr)
    print(f"Индексы: max = {arr.index(max(arr))}, min = {arr.index(min(arr))}")
    print(f"Сумма отрицательных элементов между max и min: {result}")


if __name__ == "__main__":
    main()