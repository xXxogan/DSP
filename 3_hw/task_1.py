import time
import random
import pandas as pd


def print_scheme(func):
    data = {"Размер данных": [], "Время выполнения алгоритма": []}

    for trials in range(50, 1001, 50):
        start_time = time.time()

        for _ in range(trials):
            if func.__code__.co_argcount == 1:
                x = random.randint(1, 1000)
                func(x)
            else:
                m = random.randint(1, 1000)
                n = random.randint(1, 1000)
                func(m, n)

        end_time = time.time()

        final_time = end_time - start_time

        data["Размер данных"].append(trials)
        data["Время выполнения алгоритма"].append(final_time)

    df = pd.DataFrame(data)
    return df
