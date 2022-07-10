import math
import numpy as np

START_TIMES2 = [1, 2, 3, 4, 5]
FINISH_TIMES2 = [3, 4, 5, 6, 7]

START_TIMES = [1, 2, 6, 3]
FINISH_TIMES = [5, 4, 8, 9]


def DP_schedule(start_times: list[int], finish_times: list[int]) -> int:
    # ! Need to sort by start times here
    # ! SAMPLEs are already sorted
    assert (len(start_times) == len(finish_times))
    sorted_start, sorted_finish = list(
        zip(*sorted(list(zip(start_times, finish_times)), key=lambda x: x[0])))

    dpTable = np.zeros(shape=(len(sorted_start) + 1, len(sorted_start) + 1),
                       dtype='int')
    dpTable[len(sorted_start), len(sorted_finish)] = 0

    prev_finish_time = -math.inf
    for curr in reversed(range(len(sorted_start))):
        for prev in range(len(sorted_start)):
            if sorted_start[curr] > prev_finish_time:
                take = dpTable[curr + 1, curr] + 1
                skip = dpTable[curr + 1, prev]
                if take > skip:
                    dpTable[curr, prev] = take
                    prev_finish_time = sorted_finish[curr]
                else:
                    dpTable[curr, prev] = skip
                    prev_finish_time = sorted_finish[prev]
            else:
                dpTable[curr, prev] = dpTable[curr + 1, prev]
        # ? Why does the prev reset happen here?
        # ? b/c at the end it's back to top level function call?
        # Technically prev cannot equal to curr
        prev_finish_time = -math.inf
    print(dpTable)
    return dpTable[0, 0]


if __name__ == '__main__':
    print(DP_schedule(START_TIMES2, FINISH_TIMES2))
