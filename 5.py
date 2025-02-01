"""
Помилки (номери рядків через пробіл, цей рядок - №2): !!!
"""

def non_negatives(nums):
    """Видалити з списку чисел 'nums' від'ємні елементи і повернути
    змінений список."""
    for i in range(len(nums)):
        if nums[i] < 0:
            del nums[i]

    return nums

import random

n = 10
nums = [round(random.uniform(-10, 10), 2) for i in range(n)]
print(nums)

non_negatives(nums)
print(nums)
