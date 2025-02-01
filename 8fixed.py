"""
Помилки (номери рядків через пробіл, цей рядок - №2): 7 11 15
"""

# Дан список ФИО. Найти наиболее часто встречаемое отчество.
# Если отчества нет, человек не учитывается в подсчете.

try:
    n = int(input("Введите кол-во человек: "))
    if n <= 0:
        raise ValueError("Количество человек должно быть положительным.")

    middle_names = {}
    for i in range(n):
        fio = input(f"Введите ФИО для человека {i + 1} через пробел: ").split()

        if len(fio) < 3:
            print(f"Предупреждение: у человека {i + 1} нет отчества, он не учитывается.")
            continue

        middle_name = fio[2]
        middle_names[middle_name] = middle_names.get(middle_name, 0) + 1

    if not middle_names:
        print("Ни у одного человека нет отчества.")
    else:
        most_common_middle_name = sorted(middle_names.items(), key=lambda item: item[1])[-1][0]
        print(f"Наиболее часто встречаемое отчество: {most_common_middle_name}")

    print("В расчете участвовало человек с отчествами:", sum(middle_names.values()))

except ValueError as ve:
    print(f"Ошибка: {ve}")
except IndexError:
    print("Ошибка при обработке данных: некорректный формат ввода ФИО.")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
