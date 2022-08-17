from random_inputs import randomIntArray
import random


def drive(fuel_range: int, target: int, stations: list[int]) -> list:
    currPosition = 0
    chosen_stations = []

    # If there's a solution, worst case is to visit all the gas stations
    # Prevent infinite loop
    for _ in range(len(stations)):
        # while currPosition < target:
        farthest_station_idx = stations.index(
            max(filter(lambda x: x <= currPosition + fuel_range, stations)))
        if (stations[farthest_station_idx] == target):
            return chosen_stations
        currPosition = stations[farthest_station_idx]
        chosen_stations.append(farthest_station_idx)

    # index by [-1] means take the last element
    if len(chosen_stations) == 0 or chosen_stations[-1] != target:
        raise ValueError('no solution to the given parameters')

    return chosen_stations


if __name__ == '__main__':
    '''
    The testing driver code is not included yet
    I'm not really sure how to generate inputs that are guaranteed to have a solution
    '''
    use_sample_inputs = False

    if use_sample_inputs:
        RANGE = 400
        TARGET = 950
        STATIONS = [0, 200, 375, 550, 750, 950]
        print(f'Chosen stations(index): {drive(RANGE, TARGET, STATIONS)}')
    else:
        RANGE = random.randint(1, 500)
        TARGET = random.randint(RANGE, 1000)
        STATIONS = [0] + randomIntArray(low=1,
                                        high=TARGET - 1,
                                        ordered=True,
                                        allow_duplicates=False,
                                        length=random.randint(3,
                                                              10)) + [TARGET]

        print(f'Range: {RANGE}, Target: {TARGET}\nStations: {STATIONS}')
        try:
            indices = drive(RANGE, TARGET, STATIONS)
            print(
                f'=> Chosen stations:\nIndices: {indices}\nValues: {[STATIONS[i] for i in indices]}'
            )
        except:
            print('No solution from this set of inputs')
