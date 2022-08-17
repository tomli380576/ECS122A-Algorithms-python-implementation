import numpy as np


def Knapsack_DP(VALUES: list[int], WEIGHTS: list[int],
                max_capacity: int) -> int:
    assert (len(VALUES) == len(WEIGHTS))
    '''   
    Waste a little space here to avoid messing with index offset
    Let's choose:
    - the 1st axis to be capacity values,
    - the 2nd axis to be item indexes
    '''
    num_items = len(VALUES)
    dp_table = np.zeros(shape=(max_capacity + 1, num_items), dtype='int')
    '''
    Do NOT use -1 as the 'last item' index here
    indexing by -1 on the np array will grab the element at num_items
    not num_items - 1
    '''
    LAST_ITEM = num_items - 1

    # fill in base cases
    for item in range(0, num_items):
        dp_table[0, item] = 0  # 'if capacity == 0' case

    for capacity in range(0, max_capacity + 1):
        # 'if item_index == NUM_ITEMS - 1:' case
        if (WEIGHTS[LAST_ITEM] <= capacity):
            dp_table[capacity, LAST_ITEM] = VALUES[LAST_ITEM]
        else:
            dp_table[capacity, LAST_ITEM] = 0

    # up to num_items - 2 because the recursive call will add 1
    # Traverse backwards becasue of the order of evaluation
    for item in reversed(range(num_items - 1)):
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
    sample_values_1 = [4, 5, 3, 7]
    sample_weights_1 = [2, 3, 1, 4]

    sample_values_2 = [60, 100, 120]
    sample_weights_2 = [10, 20, 30]

    sample_values_3 = [10, 40, 30, 50]
    sample_weights_3 = [5, 4, 6, 3]

    max_capacity = 50

    profit = Knapsack_DP(sample_values_2, sample_weights_2, max_capacity)
    print(f'At max_capacity {max_capacity}, The max profit is: {profit}')
