"""
Помилки (номери рядків через пробіл, цей рядок - №2): 18 22
"""

seats = [
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1]
]

def first_vacant_row(seats):
    """Повернути перший ряд, в якому є найбільше
    вільних місць та їх кількість.

    Повертається нумерація рядів із 1. Якщо вільних місць немає, повернути 0, 0.

    Параметри:
        - seats (list of list): інформація про продані квитки
                                (1 - продано, 0 - ні).

    Результат:
        - tuple (ряд, кількість місць).
    """
    max_count = 0
    max_row = 0
    for row_index, row in enumerate(seats):
        available_seats_count = row.count(0)  # 0 - пусто
        if available_seats_count > max_count:  # Виправлення знака на >
            max_row = row_index
            max_count = available_seats_count

    if max_count == 0:
        return 0, 0  # Якщо вільних місць немає

    return max_row + 1, max_count

print(first_vacant_row(seats))
