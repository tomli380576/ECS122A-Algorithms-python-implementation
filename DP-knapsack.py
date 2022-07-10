from random import randint
import numpy as np

# VALUES = [4, 5, 3, 7]
# WEIGHTS = [2, 3, 1, 4]

# VALUES = [60, 100, 120]
# WEIGHTS = [10, 20, 30]

VALUES = [10, 40, 30, 50]
WEIGHTS = [5, 4, 6, 3]
NUM_ITEMS = len(VALUES)


def knapsack_DP(max_capacity) -> int:
    assert(len(VALUES) == len(WEIGHTS))
    # Waste a little space here to avoid messing with index offset
    dp_table = np.zeros(shape=(max_capacity + 1, NUM_ITEMS), dtype='int')
    # Let's choose:
    #  the 1st axis to be capacity values,
    #  the 2nd axis to be item indexes
    LAST_ITEM = NUM_ITEMS - 1

    # fill in base cases
    for item in range(0, NUM_ITEMS):
        dp_table[0, item] = 0  # 'if capacity == 0' case

    for capacity in range(0, max_capacity + 1):
        # 'if item_index == NUM_ITEMS - 1:' case
        if (WEIGHTS[LAST_ITEM] <= capacity):
            dp_table[capacity, LAST_ITEM] = VALUES[LAST_ITEM]
        else:
            dp_table[capacity, LAST_ITEM] = 0

    # up to num_items - 2 because the recursive call will add 1
    # Traverse backwards becasue of the order of evaluation
    for item in reversed(range(NUM_ITEMS - 1)):
        for capacity in range(max_capacity + 1):
            skip = dp_table[capacity, item + 1]
            take = skip
            if capacity >= WEIGHTS[item]:
                take = dp_table[capacity - WEIGHTS[item],
                                item + 1] + VALUES[item]
            dp_table[capacity, item] = max(take, skip)

    # Return the value of initial call knapsack(max_capacity, 0)
    return dp_table[max_capacity, 0]


if __name__ == '__main__':
    max_capacity = randint(1, 100)
    print(f'At max_capacity {max_capacity}, The max profit is: {knapsack_DP(max_capacity)}')