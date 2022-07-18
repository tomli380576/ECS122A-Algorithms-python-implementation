import math
import numpy as np
from random_inputs import randomIntArray


# both prev and choice are indices
def LIS_index_based(A: list, prev: int, choice: int) -> int:
    if choice == len(A):
        return 0
    elif A[prev] >= A[choice]:
        return LIS_index_based(A, prev, choice + 1)
    else:
        take = LIS_index_based(A, choice, choice + 1) + 1
        leave = LIS_index_based(A, prev, choice + 1)
        return max(take, leave)


def LIS_DP(A_original: list) -> int:
    A = [-math.inf] + A_original
    N = len(A)
    # N + 1 for the j axis
    # becasue we need j = N as the base case
    dp_table: np.ndarray = np.zeros(shape=(N, N + 1), dtype='int')
    result = []

    # initialize base cases
    for i in range(len(A)):
        # this corresponds to `if j >= len(A)`
        # needed for all the i's
        dp_table[i, N] = 0

    for j in reversed(range(1, N)):
        for i in range(N - 1):
            if A[i] >= A[j]:
                dp_table[i, j] = dp_table[i, j + 1]
            else:
                take = dp_table[j, j + 1] + 1
                leave = dp_table[i, j + 1]
                dp_table[i, j] = max(take, leave)
                # Avoid repeating elements
                if take > leave and dp_table[i, j] > len(result):
                    result.append(A[j])

    result.reverse()
    # This corresponds to the initial call LIS(i = 0, j = 1)
    return dp_table[0, 1]


if __name__ == '__main__':
    '''
    Driver Code for testing.
    Change these 2 variables to toggle:
    - whether to run tests or run sample inputs
    - number of tests
    '''
    use_random_input = True
    num_tests = 2000

    if use_random_input:
        for _ in range(num_tests):
            random_arr = randomIntArray()
            try:
                backtracking = LIS_index_based([-math.inf] + random_arr, 0, 1) #type:ignore
                dp = LIS_DP(random_arr)
                assert (backtracking == dp)
            except:
                print(f'Broke on: {random_arr}')
        print(f'All {num_tests} cases passed!')
    else:
        sample_1 = [
            3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6
        ]
        sample_1_ans = 6

        sample_2 = [19, 7, 13, 5, 10, 20, 12, 13, 1, 20, 6, 19, 9, 9, 5]
        sample_2_ans = 5

        backtracking = LIS_index_based([-math.inf] + sample_1, 0, 1) #type:ignore
        dp = LIS_DP(sample_1)

        print(f'Longest Subsequence (Backtracking) length: {backtracking}')
        print(f'Longest Subsequence (DP) length: {dp}')
