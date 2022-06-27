import math
from typing import Union

START_TIMES = {'A': 1, 'B': 2, 'C': 6, 'D': 3}
FINISH_TIMES = {'A': 5, 'B': 4, 'C': 8, 'D': 9}

START_TIMES2 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
FINISH_TIMES2 = {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7}


def sortDictByValue(x: dict[str, int]):
    '''
    Sorts a dictionary by value
    ----
    Don't worry about the list comprehension here
    '''
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}


def RecursiveScheduling_returnCount(start_times: dict[str, int],
                                    finish_times: dict[str, int],
                                    prev_class_finish_time: Union[int, float],
                                    remaining_classes: set[str]) -> int:
    if len(remaining_classes) == 0:
        return 0

    best = 0  # represents the number of classes scheduled
    for curr_class in remaining_classes:
        # change >= to > depending on the problem
        if start_times[curr_class] >= prev_class_finish_time:

            # make choice
            take = RecursiveScheduling_returnCount(
                start_times, finish_times,
                prev_class_finish_time=finish_times[curr_class],
                remaining_classes=remaining_classes - set(curr_class)) + 1
            skip = RecursiveScheduling_returnCount(
                start_times, finish_times,
                prev_class_finish_time=prev_class_finish_time,
                remaining_classes=remaining_classes - set(curr_class))

            best = max(take, skip, best)

    return best


def RecursiveScheduling_returnList(start_times: dict[str, int],
                                   finish_times: dict[str, int],
                                   prev_class_finish_time: Union[int, float],
                                   remaining_classes: set[str]) -> list:
    if len(remaining_classes) == 0:
        return []

    best_schedule = []
    for curr_class in remaining_classes:
        if start_times[curr_class] >= prev_class_finish_time:

            # make choice
            take = RecursiveScheduling_returnList(
                start_times, finish_times,
                prev_class_finish_time=finish_times[curr_class],
                remaining_classes=remaining_classes - set(curr_class)) + [curr_class]

            skip = RecursiveScheduling_returnList(
                start_times, finish_times,
                prev_class_finish_time=prev_class_finish_time,
                remaining_classes=remaining_classes - set(curr_class))

            if max(len(take), len(skip)) <= len(best_schedule):
                continue
            if len(take) >= len(skip):
                best_schedule = take
            else:
                best_schedule = skip

    return best_schedule


if __name__ == '__main__':
    ALL_CLASSES = set(FINISH_TIMES2.keys())
    # Since we are using a set, the order might be messed up
    # Sort the schedule by starting time if necessary
    best_schedule = RecursiveScheduling_returnList(
        START_TIMES2, FINISH_TIMES2, -math.inf, ALL_CLASSES)
    best_schedule.sort(key=START_TIMES2.get)  # type: ignore
    best_count = RecursiveScheduling_returnCount(
        START_TIMES2, FINISH_TIMES2, -math.inf, ALL_CLASSES)
    print(f'The best schedule is: {best_schedule}, length: {best_count}')
