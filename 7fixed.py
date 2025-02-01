"""
Помилки (номери рядків через пробіл, цей рядок - №2): 7 12 13 14
"""

def power(x, y=2):
    """Вернуть x^y."""
    try:
        if y < 0:
            raise ValueError("Степень не может быть отрицательной.")
        if y == 0:
            return 1
        else:
            return x * power(x, y - 1)
    except RecursionError:
        print("Ошибка: превышена максимальная глубина рекурсии.")
        return None
    except ValueError as ve:
        print(f"Ошибка: {ve}")
        return None


try:
    x = int(input("x="))
    y = int(input("y="))

    result = power(x, y)
    if result is not None:
        print(result)
    else:
        print("Не удалось вычислить результат из-за ошибки.")

except ValueError:
    print("Ошибка: введите целые числа.")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
