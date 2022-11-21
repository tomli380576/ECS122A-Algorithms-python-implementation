from random_inputs import randomIntArray
import random


def drive(fuelRange: int | float, target: int, stations: list[int]) -> list[int]:
    currPosition = 0
    chosenStations = []

    # If there's a solution, worst case is to visit all the gas stations
    # Prevent infinite loop
    for _ in range(len(stations)):
        # while currPosition < target:
        farthestStationIndex = stations.index(
            max(filter(lambda x: x <= currPosition + fuelRange, stations))
        )
        if stations[farthestStationIndex] == target:
            return chosenStations
        currPosition = stations[farthestStationIndex]
        chosenStations.append(farthestStationIndex)

    # index by [-1] means take the last element
    if len(chosenStations) == 0 or chosenStations[-1] != target:
        raise ValueError("no solution to the given parameters")

    return chosenStations


if __name__ == "__main__":
    """
    The testing driver code is not included yet
    I'm not really sure how to generate inputs that are guaranteed to have a solution
    """
    use_sample_inputs = input("Randomize? (y/n) ") == "n"

    if use_sample_inputs:
        RANGE = 400
        TARGET = 950
        STATIONS = [0, 200, 375, 550, 750, 950]

        y = 12
        b = [0]
        b.append(b[-1] + 3 * y)
        b.append(b[-1] + 6 * y)
        b.append(b[-1] + 4 * y)
        b.append(b[-1] + 2 * y)
        b.append(b[-1] + 5 * y)
        # print(b)

        print(drive(7 * y, 240, sorted(b)))
        # worked = 0
        # for y in range(100000):
        #     RANGE = 2.5 * y
        #     STATIONS = [0]

        #     STATIONS.append(STATIONS[-1] + y)
        #     STATIONS.append(STATIONS[-1] + 20)
        #     STATIONS.append(STATIONS[-1] + 3 * y)
        #     STATIONS.append(STATIONS[-1] + y)
        #     STATIONS.append(STATIONS[-1] + 2 * y)

        #     TARGET = max(STATIONS)
        #     # print(sorted(STATIONS), f'range={RANGE}, target={TARGET}')

        #     try:
        #         # print(
        #         #     f'Chosen stations(index): {}'
        #         # )
        #         drive(RANGE, TARGET, sorted(STATIONS))
        #         worked += 1
        #     except:
        #         pass
        #         # print('No solution from this set of inputs')
        # print(f'{worked} inputs worked'
        # )

    else:
        RANGE = random.randint(1, 200)
        TARGET = random.randint(RANGE, 1000)
        STATIONS = (
            [0]
            + randomIntArray(
                low=1,
                high=TARGET - 1,
                ordered=True,
                allow_duplicates=False,
                length=random.randint(3, 10),
            )
            + [TARGET]
        )

        print(f"Range: {RANGE}, Target: {TARGET}\nStations: {STATIONS}")
        try:
            indices = drive(RANGE, TARGET, STATIONS)
            print(
                f"=> Chosen stations:\nIndices: {indices}\nValues: {[STATIONS[i] for i in indices]}"
            )
        except:
            print("No solution from this set of inputs")
"""
Working inputs
----
Range: 152, Target: 320
Stations: [0, 14, 73, 113, 138, 255, 320]

Range: 102, Target: 252
Stations: [0, 71, 86, 93, 111, 133, 187, 207, 230, 252]
"""
