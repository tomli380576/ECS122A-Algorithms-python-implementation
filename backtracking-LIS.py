import math
from random_inputs import randomIntArray


def LIS_FindNext(arr: list[int], curr_sequence: list) -> int:
    if len(arr) == 0:
        return len(curr_sequence)

    # index by [-1] means take the last element
    best = 0
    prev = -math.inf if len(curr_sequence) == 0 else curr_sequence[-1]

    for idx, elem in enumerate(arr):
        if elem > prev:
            curr_sequence.append(elem)
            take = LIS_FindNext(arr[idx:], curr_sequence) + 1
            if take > best:
                best = take
            else:
                curr_sequence = curr_sequence[:len(curr_sequence)]
    return best


def LIS_TakeOrSkip(arr: list[int], prev: int, choice: int) -> int:
    '''
    Note: prev_idx == -1 for initial call so that arr can directly accept inputs 
    - Otherwise we have to append [-math.inf] to the front of arr
    '''
    if choice == len(arr):
        return 0

    prev_val = -math.inf if prev == -1 else arr[prev]

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
    use_random_input = True
    num_tests = 200

    if use_random_input:
        for _ in range(num_tests):
            random_arr = randomIntArray()
            try:
                find_next_res = LIS_FindNext(random_arr, [])
                take_or_skip_res = LIS_TakeOrSkip(random_arr, -1, 0)
                assert (find_next_res == take_or_skip_res)
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

        find_next_res = LIS_FindNext(sample_2, [])
        take_or_skip_res = LIS_TakeOrSkip(sample_2, -1, 0)

        print(f'Longest Subsequence (Find Next) length: {find_next_res}')
        print(f'Longest Subsequence (Take or Skip) length: {take_or_skip_res}')
