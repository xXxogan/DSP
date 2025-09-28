from task_1 import print_scheme


def lcm(m: int, n: int):
    results = []

    for i in range(1, m * n + 1):
        if i % m == 0 and i % n == 0:
            results.append(i)

    return min(results)


print("НОК через список\n", print_scheme(lcm), "\n")


def lcm_iter(m: int, n: int):
    for i in range(max(m, n), m * n + 1):
        if i % m == 0 and i % n == 0:
            return i


print("НОК без списка\n", print_scheme(lcm_iter), "\n")


def gcd_euclide(m: int, n: int):
    while n:
        m, n = n, m % n
    return m


def lcm_euclide(m: int, n: int):
    return m * n // gcd_euclide(m, n)


print("НОК через список\n", print_scheme(lcm_euclide), "\n")
