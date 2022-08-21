from random_inputs import randomIntArray, randomLetterArray
import random


def randomStartAndFinish(num_classes: int = 6):
    '''
    Generates random test cases
    '''
    start = randomIntArray(low=1,
                           ordered=True,
                           length=num_classes,
                           allow_duplicates=False)
    finish = randomIntArray(low=min(start) + 1,
                            ordered=False,
                            length=num_classes,
                            allow_duplicates=False)

    class_names = randomLetterArray(length=num_classes, ordered=True)

    start_times = {k: v for k, v in zip(class_names, start)}
    finish_times = {k: v for k, v in zip(class_names, finish)}

    for _class in finish_times.keys():
        if finish_times[_class] <= start_times[_class]:
            base_offset = start_times[_class] - finish_times[_class]
            random_increase = random.randint(
                1, 4)  # change the 2nd argument to adjust offset
            finish_times[_class] += base_offset + random_increase

    return start_times, finish_times


def sortDictByValue(x: dict[str, int]) -> dict:
    '''
    Sorts a dictionary by value\n
    Don't worry about the list comprehension here
    '''
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}


def GreedySchedule(start_times: dict[str, int],
                   finish_times: dict[str, int]) -> list[str]:
    '''
    Sort by finish and change the order in START with it
    In this case we don't have need to permute START_TIMES
    becasue it's a dictionary and we can directly access by key in O(1)
    '''
    sorted_finish = sortDictByValue(finish_times)
    CLASSES = list(sorted_finish.keys())

    schedule = [CLASSES[0]]  # Take the earliest class

    for curr_class in CLASSES[1:]:
        prev_class = schedule[len(schedule) - 1]
        if start_times[curr_class] > finish_times[prev_class]:
            schedule.append(curr_class)
    return schedule


if __name__ == '__main__':
    use_random_inputs = input('Randomize? (y/n) ').lower() == 'y'
    if use_random_inputs:
        rand_start, rand_finish = randomStartAndFinish()
        print('Generated random schedule:')
        print(f'Start: {rand_start}')
        print(f'Finish: {rand_finish}')
        print(f'=> Best Schedule is {GreedySchedule(rand_start, rand_finish)}')
    else:
        START_TIMES = {'A': 1, 'B': 2, 'C': 6, 'D': 3}
        FINISH_TIMES = {'A': 5, 'B': 4, 'C': 8, 'D': 9}
        print('Using sample inputs:')
        print(
            f'=> Best Schedule is {GreedySchedule(START_TIMES, FINISH_TIMES)}')
