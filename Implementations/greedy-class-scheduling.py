from typing import Final
from random_inputs import randomIntArray, randomLetterArray
import random


def randomStartAndFinish(num_classes: int = 6):
    """
    Generates random test cases
    """
    start = randomIntArray(
        low=1, ordered=True, length=num_classes, allow_duplicates=False
    )
    finish = randomIntArray(
        low=min(start) + 1, ordered=False, length=num_classes, allow_duplicates=False
    )

    classNames = randomLetterArray(length=num_classes, ordered=True)

    startTimes = {k: v for k, v in zip(classNames, start)}
    finishTimes = {k: v for k, v in zip(classNames, finish)}

    for className in finishTimes.keys():
        if finishTimes[className] <= startTimes[className]:
            base_offset = startTimes[className] - finishTimes[className]
            randomIncrease = random.randint(
                1, 4
            )  # change the 2nd argument to adjust offset
            finishTimes[className] += base_offset + randomIncrease

    return startTimes, finishTimes


def sortDictByValue(x: dict[str, int], reverse=False) -> dict[str, int]:
    """
    Sorts a dictionary by value\n
    Don't worry about the list comprehension here
    """
    sortedDict = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    return dict(reversed(sortedDict.items())) if reverse else sortedDict


def greedySchedule(
    startTimes: dict[str, int], finishTimes: dict[str, int]
) -> list[str]:
    """
    Sort by finishTimes and change the order in startTimes with it
    In this case we don't have need to permute startTimes
    becasue it's a dictionary / hashmap and we can directly access by key in O(1)
    """
    sortedFinish = sortDictByValue(finishTimes)
    CLASSES: Final = list(sortedFinish.keys())

    # Take the earliest class, shorthand sytax to also make an array
    schedule = [CLASSES[0]]

    # CLASSES[1:] is the subarray starting at index 1
    for currClass in CLASSES[1:]:
        prevClass = schedule[-1]  # -1 index means the last element
        if startTimes[currClass] > finishTimes[prevClass]:  # if compatible
            schedule.append(currClass)  # take greedy choice
    return schedule


def greedySchdeuleLatestStart(
    startTimes: dict[str, int], finishTimes: dict[str, int]
) -> list[str]:
    """
    Reverse sort order because we want the class that starts the latest (largest startTime)
    """
    sortedStart = sortDictByValue(startTimes, reverse=True)
    CLASSES: Final = list(sortedStart.keys())
    schedule = [CLASSES[0]]
    for currClass in CLASSES[1:]:
        prevClass = schedule[-1]
        if finishTimes[currClass] < startTimes[prevClass]:
            schedule.append(currClass)
    return list(
        reversed(schedule)
    )  # just for readability, the array order doesn't really matter


if __name__ == "__main__":
    useRandomInputs = input("Randomize? (y/n) ").lower() == "y"
    if useRandomInputs:
        randStart, randFinish = randomStartAndFinish()
        print("Generated random schedule:")
        print(f"Start: {randStart}")
        print(f"Finish: {randFinish}")
        print(
            f"=> Best Schedule (end earliest) is {greedySchedule(randStart, randFinish)}"
        )
        print(
            f"=> Best Schedule (start latest) is {greedySchedule(randStart, randFinish)}"
        )
    else:
        START_TIMES = {"A": 1, "B": 2, "C": 6, "D": 3}
        FINISH_TIMES = {"A": 5, "B": 4, "C": 8, "D": 9}
        print("Using sample inputs:")
        print(
            f"=> Best Schedule (end earliest) is {greedySchedule(START_TIMES, FINISH_TIMES)}"
        )
        print(
            f"=> Best Schedule (start latest) is {greedySchdeuleLatestStart(START_TIMES, FINISH_TIMES)}"
        )
