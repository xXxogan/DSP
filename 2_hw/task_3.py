import random
import pandas as pd


def index_of(x: int, int_list: list):
    k = 0

    for i in range(len(int_list)):
        k += 1
        if int_list[i] == x:
            return k

    return k


def binary_search(x: int, int_list: list):
    array = sorted(int_list)
    k = 0

    left = 0
    right = len(array) - 1

    while left <= right:
        k += 1
        avg = (left + right) // 2

        if x == array[avg]:
            return k

        if x > array[avg]:
            left = avg + 1
        else:
            right = avg - 1

    return k


difficulty = {
    "Размер массива": [],
    "Сложность последовательного поиска": [],
    "Сложность двоичного поиска": [],
}


for i in range(20, 501, 20):
    int_list = [random.randint(1, 99) for _ in range(i)]
    x = random.randint(1, 99)

    ind = index_of(x, int_list)
    binar = binary_search(x, int_list)

    difficulty["Размер массива"].append(i)
    difficulty["Сложность последовательного поиска"].append(ind)
    difficulty["Сложность двоичного поиска"].append(binar)

df = pd.DataFrame(difficulty)

print(df)
