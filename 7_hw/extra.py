import random
from test_func import test
from task_1 import fast_power_mod


def diffie_hellman(p, g, a_private, b_private):
    A, _ = fast_power_mod(g, a_private, p)

    B, _ = fast_power_mod(g, b_private, p)

    s_alice, _ = fast_power_mod(B, a_private, p)

    s_bob, _ = fast_power_mod(A, b_private, p)

    return {
        "A": A,
        "B": B,
        "secret_alice": s_alice,
        "secret_bob": s_bob,
        "match": s_alice == s_bob,
    }


def params():
    primes = [23, 101, 503, 1009, 10007, 100003, 1000003]
    g = 5
    for p in primes:
        a = random.randint(2, p - 2)
        b = random.randint(2, p - 2)
        yield (p, p, g, a, b)


def dh_wrapper(p, g, a, b):
    result = diffie_hellman(p, g, a, b)
    return result["match"], 4


algorithm = [("Диффи-Хеллман", dh_wrapper)]

df = test(algorithm, params(), "Модуль p")


""" 

   Модуль p  Диффи-Хеллман (умножения)  Диффи-Хеллман (время)
0        23                          4               0.000006
1       101                          4               0.000004
2       503                          4               0.000007
3      1009                          4               0.000006
4     10007                          4               0.000007
5    100003                          4               0.000011
6   1000003                          4               0.000013

"""
