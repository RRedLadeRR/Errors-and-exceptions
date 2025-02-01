"""
Помилки (номери рядків через пробіл, цей рядок - №2): 8 16 24
"""

def f(x):
    """Вернуть значение функции.

    Функция не обрабатывает исключения.
    """
    try:
        return x**2 / (x + 2) - 3
    except ZeroDivisionError:
        return '-'

try:
    k = int(input("Введите границу интервала [-k; k]: "))
    h = float(input("Введите шаг табуляции: "))
except ValueError:
    print("Ошибка: введены некорректные значения.")
    exit(1)

x = -k
print("{:>10} {:>10}".format("x", "f(x)"))
while x <= k:
    try:
        result = f(x)
        if result == '-':
            print("{:10.2f} {:>10}".format(x, "-"))
        else:
            print("{:10.2f} {:10.2f}".format(x, result))
    except Exception as e:
        print(f"Ошибка при вычислении для x = {x}: {e}")
    
    x += h
