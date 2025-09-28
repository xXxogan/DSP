import random
import pandas as pd


def bubble_sort(array: list[int]):
    k = 0
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            k += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array, k


def binary_search(x: int, array: list[int]):
    array_sort, sort_iter = bubble_sort(array)
    k = 0

    left = 0
    right = len(array_sort) - 1

    while left <= right:
        k += 1
        avg = (left + right) // 2

        if x == array_sort[avg]:
            return k, sort_iter

        if x > array_sort[avg]:
            left = avg + 1
        else:
            right = avg - 1

    return k, sort_iter


results = {"Кол-во запросов": [], "Эффективность поиска": []}

for k in range(20, 1001, 20):
    array = [random.randint(1, 99) for _ in range(1000)]
    results["Кол-во запросов"].append(k)

    x = random.randint(1, 99)
    binary, sort_iter = binary_search(x, array)
    results["Эффективность поиска"].append(binary)

df = pd.DataFrame(results)
max_k = df["Кол-во запросов"][df["Эффективность поиска"].idxmax()]

print(df, "\n\n", "Бинарный поиск становится эффективнее при ", max_k)
print("Сложность сортировки", sort_iter)
# Можем заметить, что эффективность поиска не зависит от кол-ва запросов