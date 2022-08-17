import numpy as np
from math import inf
from random_inputs import randomIntArray


def LIS_index_based(A: list[int], prev: int, choice: int) -> int:
    ''' Both prev and choice are indices '''
    if choice == len(A):
        return 0
    elif A[prev] >= A[choice]:
        return LIS_index_based(A, prev, choice + 1)
    else:
        take = LIS_index_based(A, choice, choice + 1) + 1
        skip = LIS_index_based(A, prev, choice + 1)
        return max(take, skip)


def LIS_DP(A_original: list[int]) -> int:
    A = [-inf] + A_original
    N = len(A)
    ''' 
    N + 1 for the j axis
    becasue we need j = N as the base case
    '''
    dp_table: np.ndarray = np.zeros(shape=(N, N + 1), dtype='int')

    for prev in range(len(A)):
        '''
        Fill in the base cases.
        this corresponds to `if choice == len(A)`
        needed for all the prev's
        '''
        dp_table[prev, N] = 0

    for choice in reversed(range(1, N)):
        for prev in range(N - 1):
            if A[prev] >= A[choice]:
                dp_table[prev, choice] = dp_table[prev, choice + 1]
            else:
                take = dp_table[choice, choice + 1] + 1
                leave = dp_table[prev, choice + 1]
                dp_table[prev, choice] = max(take, leave)
    '''This corresponds to the initial call LIS(prev = 0, choice = 1)'''
    return dp_table[0, 1]


if __name__ == '__main__':
    '''
    Driver Code for testing.
    Change these 2 variables to toggle:
    - whether to run tests or run sample inputs
    - number of tests
    '''
    use_random_input = False
    num_tests = 2000

    if use_random_input:
        for _ in range(num_tests):
            random_arr = randomIntArray()
            try:
                backtracking = LIS_index_based([-inf] + random_arr, 0, 1)  # type: ignore
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

        backtracking = LIS_index_based([-inf] + sample_1, 0, 1)  #type:ignore
        dp = LIS_DP(sample_1)

        print(f'Longest Subsequence (Backtracking) length: {backtracking}')
        print(f'Longest Subsequence (DP) length: {dp}')
