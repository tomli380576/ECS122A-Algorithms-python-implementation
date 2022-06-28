import math

ITEM_VALUES = [60, 100, 120]
ITEM_WEIGHTS = [10, 20, 30]
NUM_ITEMS = len(ITEM_VALUES)


def knapsack(capacity, item_index):
    if capacity == 0:
        return 0
    if item_index == NUM_ITEMS - 1:
        if ITEM_WEIGHTS[item_index] <= capacity:
            return ITEM_VALUES[item_index]
        else:
            return 0

    best = -math.inf
    for item in range(item_index, NUM_ITEMS - 1):
        take = knapsack(capacity - ITEM_WEIGHTS[item],
                        item + 1) + ITEM_VALUES[item]
        skip = knapsack(capacity, item + 1)
        best = max(take, skip)
    return best


if __name__ == '__main__':
    assert (len(ITEM_VALUES) == len(ITEM_WEIGHTS))
    print(f'The max profit is: {knapsack(50, 0)}')
