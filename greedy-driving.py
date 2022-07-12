def drive(fuel_range, target, stations: list) -> list:
    currPosition = 0
    stations_chosen = []
    while currPosition < target:
        farthest_station_idx = stations.index(
            max(filter(lambda x: x <= currPosition + fuel_range, stations)))
        if (stations[farthest_station_idx] == target):
            return stations_chosen
        currPosition = stations[farthest_station_idx]
        stations_chosen.append(farthest_station_idx)
    return stations_chosen


if __name__ == '__main__':
    RANGE = 400
    TARGET = 950
    STATIONS = [0, 200, 375, 550, 750, 950]
    print(drive(RANGE, TARGET, STATIONS))