def num_root(x: int) -> int:
    while x > 9:
        x = x % 10 + num_root(x // 10)

    return x


num = int(input("Введите число: "))
print(f"Цифровой корень {num} = {num_root(num)}")


def factorial(x: int) -> int:
    if x == 0:
        return 1
    if x < 0:
        return -1
    return x * factorial(x - 1)


print(f"Факториал {num} = {factorial(num)}")


def sum_for_n(n: int) -> int:
    if n < 0:
        return -1
    elif n == 0:
        return 0
    return n + sum_for_n(n - 1)


print(f"Сумма чисел от 1 до {num} = {sum_for_n(num)}")
