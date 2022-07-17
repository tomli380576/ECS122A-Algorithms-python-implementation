import random
from random_inputs import randomIntArray


def Partition(nums, pivot_val):
    left = []
    right = []
    pivot_seen = False
    for num in nums:
        if num < pivot_val:
            left.append(num)
        elif num == pivot_val and not pivot_seen:
            pivot_seen = True
        elif num == pivot_val and pivot_seen:
            left.append(num)
        else:
            right.append(num)

    return left, right


def QuickSort(nums) -> list:
    if len(nums) > 1:
        pivot_val = random.choice(nums)
        left, right = Partition(nums, pivot_val)
        sorted_left = QuickSort(left)
        sorted_right = QuickSort(right)
        return sorted_left + [pivot_val] + sorted_right
    else:
        return nums


if __name__ == '__main__':
    sample_arr = [3, 1, 4, 1, 5, 9, 2]
    random_huge_list = randomIntArray(low=1, high=1000000, length=500)

    print(f'Sorted: {QuickSort(sample_arr)}')
    assert (QuickSort(random_huge_list) == sorted(random_huge_list))
