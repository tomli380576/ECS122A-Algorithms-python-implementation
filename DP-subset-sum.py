import numpy as np


def subsetSum_firstSolution(nums: list[int], curr_subset: list[int],
                            target: int) -> bool:
    # Goal state
    if target == 0:
        return True

    # No more choices but NOT goal state
    if (len(nums) == 0 or target < 0):
        return False

    for idx, num in enumerate(nums):
        # try skipping the current number
        if subsetSum_firstSolution(nums[idx + 1:], curr_subset, target):
            return True
        # skipping fails, so try including current number
        curr_subset.append(num)
        if subsetSum_firstSolution(nums[idx + 1:], curr_subset, target - num):
            return True
        else:
            #includng current one doesn't work, we must remove it
            curr_subset.pop(len(curr_subset) - 1)
    return False


def subsetSum_DP(nums: list, target: int):
    dptable = np.zeros(shape=(len(nums) + 1, target + 1))

    for num_idx, num_choice in enumerate(nums):
        for t in range(target):
            ...  #TODO

    pass


if __name__ == '__main__':
    sample_set = [
        3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6
    ]
    target = 15
    subsetSum_DP(sample_set, target)
