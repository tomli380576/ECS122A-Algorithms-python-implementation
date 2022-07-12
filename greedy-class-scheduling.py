START_TIMES = {'A': 1, 'B': 2, 'C': 6, 'D': 3}
FINISH_TIMES = {'A': 5, 'B': 4, 'C': 8, 'D': 9}


def sortDictByValue(x: dict[str, int]) -> dict:
    '''
    Sorts a dictionary by value\n
    Don't worry about the list comprehension here
    '''
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}


def greedySchedule() -> list[str]:
    # Sort by finish and change the order in START with it
    # In this case we don't have need to permute START_TIMES
    # becasue it's a dict and we can directly access by key in O(1)
    sorted_finish = sortDictByValue(FINISH_TIMES)
    CLASSES = list(sorted_finish.keys())

    schedule = [CLASSES[0]]  # Take the earliest class

    for curr_class in CLASSES[1:]:
        last_class = schedule[len(schedule) - 1]
        if START_TIMES[curr_class] > FINISH_TIMES[last_class]:
            schedule.append(curr_class)
    return schedule


if __name__ == '__main__':
    print(f'Best Schedule is {greedySchedule()}')
