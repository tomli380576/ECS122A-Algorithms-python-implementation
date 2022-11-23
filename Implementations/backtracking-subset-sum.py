from random_inputs import randomIntArray
from random import randint


def SubsetSum_First(nums: list[int], curr_subset: list[int], target: int) -> bool:
    """
    Find the first working solution
    """

    # Goal state
    if target == 0:
        return True

    # No more choices but NOT goal state
    if len(nums) == 0 or target < 0:
        return False

    for idx, num in enumerate(nums):
        # try skipping the current number
        if SubsetSum_First(nums[idx + 1 :], curr_subset, target):
            return True
        # skipping fails, so try including current number
        curr_subset.append(num)
        if SubsetSum_First(nums[idx + 1 :], curr_subset, target - num):
            return True
        else:
            # includng current one doesn't work, we must remove it
            curr_subset.pop()
    return False


def SubsetSum_All(
    nums: list[int],
    curr_subset: list[int],
    target: int,
    working_subsets: list[list[int]],
) -> None:
    """
    Find all the unique solutions
    """

    # Goal state
    if target == 0 and curr_subset not in working_subsets:
        working_subsets.append(curr_subset)
        return

    # No more choices but NOT goal state
    if len(nums) == 0 or target < 0:
        return

    for idx, num in enumerate(nums):
        """
        Always try including the choice,
            if it doesn't work,
            we automatically fall back to the 'skip' case
            by moving on to the next num
        The base case will do the check of whether it works or not
        """
        SubsetSum_All(
            nums[idx + 1 :], curr_subset + [num], target - num, working_subsets
        )


if __name__ == "__main__":
    sample_set = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]

    random_arr = randomIntArray(0, 30, 15, allow_duplicates=False)
    rand_target = randint(min(random_arr), sum(random_arr) // 2)

    print(f"Random array: {random_arr}, target = {rand_target}")
    # c and w are temporary arrays to hold the results
    c = []
    SubsetSum_First(nums=random_arr, curr_subset=c, target=rand_target)
    print(f"The first solution found is: {c}")

    w = []
    print(f"Looking for all solutions:")
    SubsetSum_All(
        nums=random_arr, curr_subset=[], target=rand_target, working_subsets=w
    )
    for i in range(len(w)):
        w[i] = sorted(w[i])
    w.sort()
    for i in w:
        print(i)
    print(f"There are {len(w)} possible unique solutions.")
