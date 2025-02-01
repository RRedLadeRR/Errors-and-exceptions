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

import random

random.seed(50)

N_MAX = 10
RANGE_MIN = 1
RANGE_MAX = 100
nums = random.sample(range(RANGE_MIN, RANGE_MAX), N_MAX)

print(nums)

print(min_pair(nums))
