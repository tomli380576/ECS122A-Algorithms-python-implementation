from random import randint
from random_inputs import randomIntArray
from math import inf

def Knapsack_TakeOrSkip(VALUES, WEIGHTS, capacity, item_index=0):
    if len(VALUES) != len(WEIGHTS):
        raise ValueError(
            'Invalid input, values and weights have different lengths')

    if capacity == 0:
        return 0

    if item_index == len(VALUES) - 1:
        if WEIGHTS[item_index] <= capacity:
            return VALUES[item_index]
        else:
            return 0

    skip = Knapsack_TakeOrSkip(VALUES, WEIGHTS, capacity, item_index + 1)
    take = skip

    if capacity >= WEIGHTS[item_index]:
        take = Knapsack_TakeOrSkip(VALUES, WEIGHTS,
                                   capacity - WEIGHTS[item_index],
                                   item_index + 1) + VALUES[item_index]

    return max(take, skip)


def Knapsack_FindNext(VALUES, WEIGHTS, capacity, item_index=0):
    if capacity == 0:
        return 0

    if item_index == len(VALUES) - 1:
        if WEIGHTS[item_index] <= capacity:
            return VALUES[item_index]
        else:
            return 0

    best = -inf
    for choice in range(item_index, len(VALUES)):
        skip = Knapsack_FindNext(VALUES, WEIGHTS, capacity, choice + 1)
        take = skip

        if WEIGHTS[choice] <= capacity:
            take = Knapsack_FindNext(VALUES, WEIGHTS,
                                     capacity - WEIGHTS[choice],
                                     choice + 1) + VALUES[choice]
        best = max(best, take, skip)

    return best


if __name__ == '__main__':
    '''
    Driver Code for testing.
    Change these 2 variables to toggle:
    - whether to run tests or run sample inputs
    - number of tests
    '''
    use_random_input = True
    num_tests = 500

    if use_random_input:
        for _ in range(num_tests):
            num_items = randint(3, 10)
            ITEM_VALUES = randomIntArray(10,
                                        500,
                                        length=num_items,
                                        allow_duplicates=False)
            ITEM_WEIGHTS = randomIntArray(10,
                                        50,
                                        length=num_items,
                                        allow_duplicates=False)
            max_capacity = randint(min(ITEM_WEIGHTS), sum(ITEM_WEIGHTS))
            take_or_skip = Knapsack_TakeOrSkip(ITEM_VALUES, ITEM_WEIGHTS,
                                            max_capacity)
            find_next = Knapsack_FindNext(ITEM_VALUES, ITEM_WEIGHTS, max_capacity)
            try:
                assert (take_or_skip == find_next)
            except:
                print(f'Broke on: values={ITEM_VALUES}, weights={ITEM_WEIGHTS}')
        print(f'All {num_tests} cases passed!')
    
    else:
        ITEM_VALUES = [60, 100, 120]
        ITEM_WEIGHTS = [10, 20, 30]
        max_capacity = 50
        print(
            f'At max_capacity {max_capacity}, The max profit is: {Knapsack_TakeOrSkip(ITEM_VALUES, ITEM_WEIGHTS, max_capacity)}'
        )
        print(
            f'At max_capacity {max_capacity}, The max profit is: {Knapsack_FindNext(ITEM_VALUES, ITEM_WEIGHTS, max_capacity)}'
        )
