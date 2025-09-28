from task_1 import print_scheme


def gсd(m: int, n: int):
    list_of_divisors = []

    for i in range(1, min(m, n) + 1):
        if m % i == 0 and n % i == 0:
            list_of_divisors.append(i)

    return max(list_of_divisors)


print("НОД с массивом\n", print_scheme(gсd), "\n")


def gcd_iter(m: int, n: int):
    gcd = 1

    for i in range(1, min(m, n) + 1):
        if m % i == 0 and n % i == 0:
            gcd = i

    return gcd


print("НОД с заменой переменной\n", print_scheme(gcd_iter), "\n")


def gcd_reverse(m: int, n: int):
    gcd = 1

    for i in range(min(m, n) + 1, 1, -1):
        if m % i == 0 and n % i == 0:
            gcd = i

    return gcd


print("НОД обратный\n", print_scheme(gcd_reverse), "\n")


def gcd_euclide(m: int, n: int):
    while n:
        m, n = n, m % n
    return m


print("НОД Евклида\n", print_scheme(gcd_euclide), "\n")
