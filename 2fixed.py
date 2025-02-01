"""
Помилки (номери рядків через пробіл, цей рядок - №2): 6 10
"""

def primes(a, b):
    """Повернути список простих чисел на відрізку від 'a' до 'b'."""
    res = []
    for i in range(a, b + 1):
        if i > 1:  # Прості числа більше 1
            c = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    c += 1
            if c == 2:
                res.append(i)
    return res
