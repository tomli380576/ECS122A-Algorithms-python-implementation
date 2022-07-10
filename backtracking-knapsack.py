import math
from random import randint

# ITEM_VALUES = [60, 100, 120]
# ITEM_WEIGHTS = [10, 20, 30]
ITEM_VALUES = [10, 40, 30, 50]
ITEM_WEIGHTS = [5, 4, 6, 3]
NUM_ITEMS = len(ITEM_VALUES)


def knapsack(capacity, item_index=0):
    assert (len(ITEM_VALUES) == len(ITEM_WEIGHTS))

    if capacity == 0:
        return 0

    if item_index == NUM_ITEMS - 1:
        if ITEM_WEIGHTS[item_index] <= capacity:
            return ITEM_VALUES[item_index]
        else:
            return 0

    best = -math.inf
    for item in range(item_index, NUM_ITEMS):
        skip = knapsack(capacity, item + 1)
        take = skip
        if capacity >= ITEM_WEIGHTS[item]:
            take = knapsack(capacity - ITEM_WEIGHTS[item],
                            item + 1) + ITEM_VALUES[item]
        best = max(best, take, skip)
    return best


if __name__ == '__main__':

    max_capacity = randint(1, 100)
    print(
        f'At max_capacity {max_capacity}, The max profit is: {knapsack(max_capacity)}'
    )
