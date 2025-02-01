"""
Помилки (номери рядків через пробіл, цей рядок - №2): 5 7
"""

def min_pair(nums):
    """Повернути мінімальну суму сусідніх 2-х чисел у списку 'nums'."""
    min_sum = nums[0] + nums[1]  # Виправлено добуток на суму
    for i in range(len(nums) - 1):  # Перевіряємо всі сусідні пари
        current_sum = nums[i] + nums[i + 1]
        min_sum = min(current_sum, min_sum)  # Використовуємо функцію min()

    return min_sum
