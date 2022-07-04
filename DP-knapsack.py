import numpy as np

ITEM_VALUES = [60, 100, 120]
ITEM_WEIGHTS = [10, 20, 30]
NUM_ITEMS = len(ITEM_VALUES)


def knapsack_DP(max_capacity) -> int:
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
        if (ITEM_WEIGHTS[LAST_ITEM] <= capacity):
            dp_table[capacity, LAST_ITEM] = ITEM_VALUES[LAST_ITEM]
        else:
            dp_table[capacity, LAST_ITEM] = 0

    # up to num_items - 2 because the recursive call will add 1
    # Traverse backwards becasue of the order of evaluation
    for item in reversed(range(0, NUM_ITEMS - 1)):
        # The direction of the capacity loop doesn't matter
        for capacity in range(0, max_capacity + 1):
            take = dp_table[capacity - ITEM_WEIGHTS[item],
                            item + 1] + ITEM_VALUES[item]
            skip = dp_table[capacity, item + 1]
            dp_table[capacity, item] = max(take, skip)

    # Return the value of initial call knapsack(max_capacity, 0)
    return dp_table[max_capacity, 0]


if __name__ == '__main__':
    print(f'The max profit is: {knapsack_DP(50)}')
