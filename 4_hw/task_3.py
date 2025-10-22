def log_recursive(m: int, n: int) -> int:
    return 0 if n < m else 1 + log_recursive(m, n // m)


base = int(input("Введите основание логарифма: "))
value = int(input("Введите значение логарифма: "))

print(
    f"Рекурсивный логарифм от {value} по основанию {base} приближенно равен {log_recursive(base, value)}"
)
