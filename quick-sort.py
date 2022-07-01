CYAN = '\033[96m'
END_COLOR = '\033[0m'  # for command line colors


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


def quicksort(nums: list,
              left: int,
              right: int,
              showIntermediateSteps=False) -> list:
    if len(nums) == 1:
        return nums
    if left < right:
        # sort the single pivot first
        pivot = partition(nums, left, right)
        if showIntermediateSteps:
            print(
                f'{nums[left:pivot - 1]}\b, {CYAN}{nums[pivot]}{END_COLOR}, {str(nums[pivot + 1: right])[1:]}'
            )

        quicksort(nums, left, pivot - 1)  # Recursively sorting the left values
        quicksort(nums, pivot + 1,
                  right)  # Recursively sorting the right values
    return nums


if __name__ == '__main__':
    sample_arr = [
        3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6
    ]
    print(f'Original: {sample_arr}')
    quicksort(nums=sample_arr, left=0, right=len(sample_arr) - 1)
    print(f'Sorted: {sample_arr}')
