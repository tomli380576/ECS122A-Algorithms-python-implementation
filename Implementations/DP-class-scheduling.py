from math import inf
import numpy as np


def DP_schedule(start_times: list[int], finish_times: list[int]) -> int:
    assert (len(start_times) == len(finish_times))
    '''
    sort finish and permute start with it
    '''
    sorted_start, sorted_finish = list(
        zip(*sorted(list(zip(start_times, finish_times)), key=lambda x: x[0])))

    dp_table = np.zeros(shape=(len(sorted_start) + 1, len(sorted_start) + 1),
                        dtype='int')
    dp_table[len(sorted_start), len(sorted_finish)] = 0

    prev_finish_time = -inf
    for curr in reversed(range(len(sorted_start))):
        for prev in range(len(sorted_start)):
            if sorted_start[curr] > prev_finish_time:
                take = dp_table[curr + 1, curr] + 1
                skip = dp_table[curr + 1, prev]
                if take > skip:
                    dp_table[curr, prev] = take
                    prev_finish_time = sorted_finish[curr]
                else:
                    dp_table[curr, prev] = skip
                    prev_finish_time = sorted_finish[prev]
            else:
                dp_table[curr, prev] = dp_table[curr + 1, prev]
        '''
        Reset the prev_finish_time here
        We tried everything with 'curr' as the first class (line 18)
        so we have to reset to choose the next 'first class'
        '''
        prev_finish_time = -inf

    return dp_table[0, 0]


if __name__ == '__main__':

    START_TIMES1 = [1, 2, 6, 3]
    FINISH_TIMES1 = [5, 4, 8, 9]

    START_TIMES2 = [1, 2, 3, 4, 5]
    FINISH_TIMES2 = [3, 4, 5, 6, 7]

    print(f'Max number of classes: {DP_schedule(START_TIMES1, FINISH_TIMES1)}')
