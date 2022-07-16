
# Source: https://www.geeksforgeeks.org/quick-sort/
def partition_inplace(nums: list, left: int, right: int) -> int:
    # swap the last element with pivot
    pivot, num_lt_pivot = nums[right], left

    # right is not included in range
    for i in range(left, right):
        if nums[i] <= pivot:
            nums[i], nums[num_lt_pivot] = nums[num_lt_pivot], nums[i]
            num_lt_pivot += 1

    nums[num_lt_pivot], nums[right] = nums[right], nums[num_lt_pivot]
    return num_lt_pivot


def quicksort_inplace(nums: list,
                      left: int,
                      right: int,
                      showIntermediateSteps=False) -> list:

    CYAN = '\033[96m'
    END_COLOR = '\033[0m'  # for command line colors

    if len(nums) == 1:
        return nums
    if left < right:
        pivot = partition_inplace(nums, left, right)
        if showIntermediateSteps:
            print(
                f'{nums[left:pivot - 1]}\b, {CYAN}{nums[pivot]}{END_COLOR}, {str(nums[pivot + 1: right])[1:]}'
            )

        quicksort_inplace(nums, left, pivot - 1)
        quicksort_inplace(nums, pivot + 1, right)
    return nums
