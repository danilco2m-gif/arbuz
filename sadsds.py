result = []

def divider(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Один из аргументов не является числом")
    if b == 0:
        raise ValueError("Делить на ноль нельзя")
    if a > 100:
        raise IndexError("Значение больше 100")
    return a / b

data = {10: 2, 25: 5, '123': 4, 18: 0, 8: 4}
for key, value in data.items():
    try:
        res = divider(key, value)
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f"Ошибка при обработке {key}: {e}")

print(result)
