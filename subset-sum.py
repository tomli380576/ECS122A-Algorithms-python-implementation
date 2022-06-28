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


def subsetSum_allSolutions(nums: list[int], curr_subset: list[int],
                           target: int,
                           working_subsets: list[list[int]]) -> None:
    # Goal state
    if target == 0 and curr_subset not in working_subsets:
        working_subsets.append(curr_subset)

    # No more choices but NOT goal state
    if (len(nums) == 0 or target < 0):
        return

    for idx, num in enumerate(nums):
        # always try including the choice
        # if it doesn't work, we automatically falls back to the 'skip' case by moving on to the next
        # The base case will do the check of whether it works or not
        subsetSum_allSolutions(nums[idx + 1:], curr_subset + [num],
                               target - num, working_subsets)


if __name__ == '__main__':
    sample_set = [
        3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6
    ]

    # c and w are temporary arrays to hold the results
    c = []
    subsetSum_firstSolution(nums=sample_set, curr_subset=c, target=15)
    print(f'The first solution it found is: {c}')

    w = []
    subsetSum_allSolutions(nums=sample_set,
                           curr_subset=[],
                           target=15,
                           working_subsets=w)
    print(f'There are {len(w)} possible unique solutions.')
