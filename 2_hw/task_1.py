import random

int_list = [random.randint(1, 99) for _ in range(10)]


def index_of(x: int):
    k = 0

    for i in range(len(int_list)):
        if int_list[i] == x:
            k += 1
            return i, k
        k += 1

    return -1, k


print(int_list)
x = input("Введите число: ")
print("Индекс, кол-во итераций: ", index_of(x))
