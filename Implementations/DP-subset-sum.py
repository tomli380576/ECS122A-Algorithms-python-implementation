import numpy as np
from random_inputs import randomIntArray
from random import randint


def SubsetSum_First(nums: list[int], curr_subset: list[int], target: int) -> bool:
    """
    Backtracking code for reference
    """

    if target == 0:  # Goal state
        # print curr_subset here to see the actual subset
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
            curr_subset.pop(len(curr_subset) - 1)
    return False


def SubsetSum_DP(nums: list[int], final_target: int) -> bool:
    dp_table = np.empty(shape=(len(nums) + 1, final_target + 1), dtype=np.bool_)
    """ 
    Order of Evalutaion,
    + 1 in range function is to force include len(nums) and final_target
    """
    for i in reversed(range(0, len(nums) + 1)):
        for target in range(final_target + 1):
            if target == 0:
                dp_table[i, target] = True
                continue
            elif i == len(nums):
                dp_table[i, target] = False
                continue

            if target - nums[i] >= 0:
                """
                Take is only valid if target - nums[i] is not negative
                Otherwise we defeinitely don't have a solution and we run into indexing problems
                """
                skip = dp_table[i + 1, target]
                take = dp_table[i + 1, target - nums[i]]
                dp_table[i, target] = take or skip
            else:
                """Must skip if target - nums[i] < 0"""
                skip = dp_table[i + 1, target]
                dp_table[i, target] = skip
    """ Simulate initial call """
    return dp_table[0, final_target]


if __name__ == "__main__":
    run_random_cases = input("Randomize? (y/n) ").lower() == "y"
    verbose = run_random_cases and input("Verbose outputs? (y/n) ").lower() == "y"
    num_tests = 1000

    if run_random_cases:
        print(f"Using radom inputs.")
        all_passed = True
        for _case in range(num_tests):
            random_arr = randomIntArray(0, 30, 15, allow_duplicates=False)
            rand_target = randint(min(random_arr), sum(random_arr) // 2)
            try:
                c = []
                assert SubsetSum_DP(random_arr, rand_target) == SubsetSum_First(
                    random_arr, c, rand_target
                )
            except:
                print(f"Broke on {random_arr}, target = {rand_target}")
                all_passed = False
            else:
                if verbose:
                    print(f"Case {_case} passed")
        if all_passed:
            print(f"All {num_tests} cases passed!")
    else:
        print(f"Using sample inputs.")
        sample_set = [
            3,
            1,
            4,
            1,
            5,
            9,
            2,
            6,
            5,
            3,
            5,
            8,
            9,
            7,
            9,
            3,
            2,
            3,
            8,
            4,
            6,
            2,
            6,
        ]
        sample_target = 15
        # answer is true, for example [1, 9, 5] is a solution

        print("DP:", SubsetSum_DP(sample_set, sample_target))
