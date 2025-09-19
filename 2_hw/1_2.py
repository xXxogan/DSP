import random

array = sorted([random.randint(1, 99) for _ in range(10)])


def binary_search(x: int):
    k = 0

    left = 0
    right = len(array) - 1

    while left <= right:
        k += 1
        avg = (left + right) // 2

        if x == array[avg]:
            return True, k

        if x > array[avg]:
            left = avg + 1
        else:
            right = avg - 1

    return False, k


print(array)
x = int(input("Введите число: "))
print("Содержится ли число, кол-во итераций", binary_search(x))
