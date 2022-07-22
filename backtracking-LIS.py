from math import inf
from random_inputs import randomIntArray


def LIS_FindNext(A: list[int], prev: int, choice: int) -> int:
    '''
    Note: prev_idx is set to -1 for initial call
    - Otherwise we have to append [-math.inf] to the front of arr
    '''

    if len(A) == 0:
        return 0

    # index by [-1] means take the last element
    prev_val = -inf if prev == -1 else A[prev]

    best = 0
    for idx in range(choice, len(A)):
        if A[idx] > prev_val:
            take = LIS_FindNext(A, idx, idx + 1) + 1
            if take > best:
                best = take
    return best


def LIS_TakeOrSkip(arr: list[int], prev: int, choice: int) -> int:
    if choice == len(arr):
        return 0

    prev_val = -inf if prev == -1 else arr[prev]

    skip = LIS_TakeOrSkip(arr, prev, choice + 1)
    take = skip
    choice_val = arr[choice]

    if choice_val > prev_val:
        take = LIS_TakeOrSkip(arr, choice, choice + 1) + 1

    return max(skip, take)


if __name__ == '__main__':
    '''
    Driver Code for testing.
    Change these 2 variables to toggle:
    - whether to run tests or run sample inputs
    - number of tests
    '''
    use_random_input = False
    num_tests = 200

    if use_random_input:
        for _ in range(num_tests):
            random_arr = randomIntArray()
            try:
                find_next_res = LIS_FindNext(random_arr, -1, 0)
                take_or_skip_res = LIS_TakeOrSkip(random_arr, -1, 0)
                assert (find_next_res == take_or_skip_res)
            except:
                print(f'Broke on: {random_arr}')
                exit()
        print(f'All {num_tests} cases passed!')
    else:
        sample_1 = [
            3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6
        ]
        sample_1_ans = 6

        sample_2 = [19, 7, 13, 5, 10, 20, 12, 13, 1, 20, 6, 19, 9, 9, 5]
        sample_2_ans = 5

        find_next_res = LIS_FindNext(sample_1, -1, 0)
        take_or_skip_res = LIS_TakeOrSkip(sample_1, -1, 0)

        print(f'Longest Subsequence (Find Next) length: {find_next_res}')
        print(f'Longest Subsequence (Take or Skip) length: {take_or_skip_res}')
