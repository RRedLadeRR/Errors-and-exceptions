"""
Помилки (номери рядків через пробіл, цей рядок - №2): 7 11 12 14
"""

def unemployment_rate(unemployed, employed):
    """Вернуть уровень безработицы (УБ) в долях 1.

       Расчет по формуле: УБ = Безработные / (Занятые + Безработные).
    """
    try:
        total = unemployed + employed
        if total == 0:
            raise ZeroDivisionError("Общее количество людей не может быть нулевым.")
        if unemployed < 0 or employed < 0:
            raise ValueError("Количество безработных и занятых не может быть отрицательным.")
        return unemployed / total
    except ZeroDivisionError as zde:
        print(f"Ошибка: {zde}")
        return None
    except ValueError as ve:
        print(f"Ошибка: {ve}")
        return None


try:
    unemployed = int(input("Введите кол-во безработных (чел.): "))
    employed = int(input("Введите кол-во занятых (чел.): "))

    rate = unemployment_rate(unemployed, employed)

    if rate is not None:
        print("Уровень безработицы = {:.1%}".format(rate))
    else:
        print("Невозможно рассчитать уровень безработицы из-за некорректных данных.")

except ValueError:
    print("Ошибка: введите целые числа.")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
