import math
import numpy as np


def BruteForceSelect(arr: list[int], k) -> int:
    return sorted(arr)[k]


def partition(nums: list, left: int, right: int) -> int:
    # swap the last element with pivot
    pivot, num_lt_pivot = nums[right], left

    # right is not included in range
    for i in range(left, right):
        if nums[i] <= pivot:
            nums[i], nums[num_lt_pivot] = nums[num_lt_pivot], nums[i]
            num_lt_pivot += 1

    nums[num_lt_pivot], nums[right] = nums[right], nums[num_lt_pivot]
    return num_lt_pivot


def QuickSelect(arr: list) -> int:
    # TODO

    pass
