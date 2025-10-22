def fib_basic(n: int) -> int:
    return fib_basic(n - 1) + fib_basic(n - 2) if n > 2 else n


# print("Рекурсивно без кэш")
# for i in range(35):
#     print(i, fib_basic(i))


cash = [-1] * 1000000


def reset_cash(n: int):
    cash[0] = 0
    cash[1] = 1
    for i in range(2, n + 1):
        cash[i] = -1


def fib_cash(n: int) -> int:
    if cash[n] == -1:
        cash[n] = fib_cash(n - 1) + fib_cash(n - 2)
    return cash[n]


# print("\nРекурсивно с кэш")
# for i in range(1000):
#     reset_cash(i)
#     print(i, fib_cash(i))


def fib_iter_list(n: int) -> int:
    fibs = [-1] * (n + 1)
    fibs[0] = 0
    fibs[1] = 1
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs[-1]


# print(*fib_iter_list(100), sep=" | ")


def fib_iter_fly(n: int) -> int:
    f0 = 0
    f1 = 1
    f2 = 1
    for _ in range(2, n + 1):
        f2 = f0 + f1
        f0 = f1
        f1 = f2
    return f2


# fib_iter_fly(100)
