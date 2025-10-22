num = int(input("Введите число: "))


def n_to_1(n: int) -> None:
    print(n)
    if n > 1:
        n_to_1(n - 1)
    if n < 1:
        n_to_1(n + 1)


print(f"Процедура от {num} до 1:")
n_to_1(num)


def n_to_n(n: int) -> None:
    if n != 0:
        print(-n)
        if n > 0:
            n_to_n(n - 1)
        else:
            n_to_n(n + 1)
        print(n)
    else:
        print(0)


print(f"\nПроцедура от {-num} до {num}:")
n_to_n(num)


def n_to_n_odd(n: int) -> None:
    if n != 0:
        if n % 2 != 0:
            print(-n)
        if n > 0:
            n_to_n_odd(n - 1)
        if n < 0:
            n_to_n_odd(n + 1)
        if n % 2 != 0:
            print(n)
    else:
        print(0)


print(f"\nПроцедура от {-num} до {num} нечетные:")
n_to_n_odd(num)
