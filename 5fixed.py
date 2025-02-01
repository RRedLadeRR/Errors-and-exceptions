"""
Помилки (номери рядків через пробіл, цей рядок - №2): 8
"""

def non_negatives(nums):
    """Видалити з списку чисел 'nums' від'ємні елементи і повернути
    змінений список."""
    nums[:] = [x for x in nums if x >= 0]
    return nums

import random

n = 10
nums = [round(random.uniform(-10, 10), 2) for i in range(n)]
print(nums)

non_negatives(nums)
print(nums)
