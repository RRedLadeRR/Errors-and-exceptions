"""
Помилки (номери рядків через пробіл, цей рядок - №2): !!!
"""

def sum_of_digits(n):
    """Повернути суму цифр менших 5 для позитивного цілого числа `n`.
    Якщо таких цифр немає, повернути 0."""
    с = 0
    while n > 0:
        digit = n // 10
        if digit < 5:
            c = с + 1
        n //= 10
    return digit
