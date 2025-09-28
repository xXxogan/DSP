from task_1 import print_scheme
from math import sqrt


def is_prime_basic(value: int):
    for i in range(2, value):
        if value % i == 0:
            return False
        return True


print("Стандартный перебор\n", print_scheme(is_prime_basic), "\n")


def is_prime_odd(value: int):
    if value == 2:
        return True
    else:
        for i in range(1, value, 2):
            if value % i == 0:
                return False
            return True


print("Перебор нечетных\n", print_scheme(is_prime_odd), "\n")


def is_prime_sqrt(value: int):
    for i in range(1, value ** 0.5):
        if value % i == 0:
            return False
        return True


print("Перебор до корня числа\n", print_scheme(is_prime_odd), "\n")


def is_prime_sqrt_odd(value: int):
    if value == 2:
        return True
    else:
        for i in range(1, int(value ** 0.5), 2):
            if value % i == 0:
                return False
            return True


print("Перебор нечетных до корня\n", print_scheme(is_prime_sqrt_odd), "\n")
