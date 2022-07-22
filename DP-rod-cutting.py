import numpy as np
from time import time

PRICES = [1, 5, 8, 9, 10, 17, 17, 20]  # some price values


def cutRod(rod_len) -> int:
    if rod_len == 0:
        return 0
    if rod_len == 1:
        return PRICES[0]

    best = 0

    for i in range(1, rod_len + 1):
        price_if_make_cut = cutRod(rod_len - i) + PRICES[i - 1]
        best = max(best, price_if_make_cut)

    return best


def cutRod_DP(max_rod_len) -> int:
    dpTable = np.zeros(shape=(max_rod_len + 1), dtype='int')
    ''' 
    if rod_len == 0: return 0
    if rod_len == 1: return PRICES[0]
    '''
    dpTable[0] = 0  
    dpTable[1] = PRICES[0]  

    ''' for each missing entry'''
    for rod_len in range(2, max_rod_len + 1):
        best = 0
        ''' This is the loop on line 15'''
        for choice in range(1, rod_len + 1):
            price_if_make_cut = dpTable[rod_len - choice] + PRICES[choice - 1]
            best = max(best, price_if_make_cut)

        dpTable[rod_len] = best

    return dpTable[max_rod_len]


if __name__ == '__main__':
    start = time()
    print(f'Backtracking: {cutRod(len(PRICES))}')
    end = time()
    print(f'Time: {end - start}s')

    start = time()
    print(f'DP: {cutRod_DP(len(PRICES))}')
    end = time()
    print(f'Time: {end - start}s')
