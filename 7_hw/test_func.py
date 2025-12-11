import time
import pandas as pd


def test(algorithms, param_generator, param_name):
    data = {param_name: []}

    for name, _ in algorithms:
        data[f"{name} (умножения)"] = []
        data[f"{name} (время)"] = []

    for params in param_generator:
        data[param_name].append(params[0])

        for name, func in algorithms:
            start = time.time()
            _, mults = func(*params[1:])
            elapsed = time.time() - start

            data[f"{name} (умножения)"].append(mults)
            data[f"{name} (время)"].append(elapsed)

    df = pd.DataFrame(data)
    print(df)
