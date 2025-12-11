from test_func import test


def naive_power_mod(base, exp, mod):
    result = 1
    multiplications = 0

    for _ in range(exp):
        result = (result * base) % mod
        multiplications += 1

    return result, multiplications


def fast_power_mod(base, exp, mod):
    result = 1
    multiplications = 0
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
            multiplications += 1
        base = (base * base) % mod
        multiplications += 1
        exp //= 2

    return result, multiplications


if __name__ == "__main__":

    def params():
        base = 7
        mod = 1000000007
        for exp in range(50, 1001, 50):
            yield (exp, base, exp, mod)

    algorithms = [("Наивный", naive_power_mod), ("Быстрый", fast_power_mod)]

    df = test(algorithms, params(), "Степень")

""" 

    Степень  Наивный (умножения)  Наивный (время)  Быстрый (умножения)  Быстрый (время)
0        50                   50         0.000005                    9     2.861023e-06
1       100                  100         0.000006                   10     9.536743e-07
2       150                  150         0.000009                   12     9.536743e-07
3       200                  200         0.000011                   11     7.152557e-07
4       250                  250         0.000014                   14     9.536743e-07
5       300                  300         0.000018                   13     1.907349e-06
6       350                  350         0.000022                   15     1.907349e-06
7       400                  400         0.000025                   12     2.145767e-06
8       450                  450         0.000028                   13     1.907349e-06
9       500                  500         0.000031                   15     1.907349e-06
10      550                  550         0.000035                   14     1.192093e-06
11      600                  600         0.000038                   14     9.536743e-07
12      650                  650         0.000041                   14     1.192093e-06
13      700                  700         0.000043                   16     2.145767e-06
14      750                  750         0.000045                   17     7.152557e-07
15      800                  800         0.000047                   13     9.536743e-07
16      850                  850         0.000051                   15     2.145767e-06
17      900                  900         0.000054                   14     2.145767e-06
18      950                  950         0.000057                   17     1.192093e-06
19     1000                 1000         0.000060                   16     9.536743e-07

"""
