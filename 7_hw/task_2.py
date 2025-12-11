import math
import random
from test_func import test


def discrete_brute(base, target, mod):
    multiplications = 0
    current = 1

    for x in range(mod):
        if current == target:
            return x, multiplications
        current = (current * base) % mod
        multiplications += 1

    return None, multiplications


def discrete_bsgs(base, target, mod):
    m = math.ceil(math.sqrt(mod))
    multiplications = 0

    baby_steps = {}
    current = 1
    for j in range(m):
        baby_steps[current] = j
        current = (current * base) % mod
        multiplications += 1

    base_inv_m = pow(base, mod - 1 - m, mod)

    gamma = target
    for i in range(m):
        if gamma in baby_steps:
            x = i * m + baby_steps[gamma]
            return x, multiplications
        gamma = (gamma * base_inv_m) % mod
        multiplications += 1

    return None, multiplications


if __name__ == "__main__":

    def params():
        primes = [101, 251, 503, 1009, 2003, 3001, 5003, 7001, 10007]
        base = 5
        for p in primes:
            target = pow(base, random.randint(1, p - 1), p)
            yield (p, base, target, p)

    algorithms = [("Перебор", discrete_brute), ("BSGS", discrete_bsgs)]

    df = test(algorithms, params(), "Модуль")


""" 

   Модуль  Перебор (умножения)  Перебор (время)  BSGS (умножения)  BSGS (время)
0     101                   15     1.907349e-06                12      0.000006
1     251                    7     9.536743e-07                16      0.000003
2     503                  315     2.002716e-05                36      0.000005
3    1009                  149     9.059906e-06                36      0.000005
4    2003                 1099     6.294250e-05                69      0.000007
5    3001                  220     1.192093e-05                59      0.000007
6    5003                  475     2.598763e-05                77      0.000007
7    7001                 1113     6.198883e-05                97      0.000011
8   10007                 8455     4.663467e-04               184      0.000016

"""
