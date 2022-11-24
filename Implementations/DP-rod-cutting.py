import numpy as np
from time import time
from random_inputs import randomIntArray

PRICES = [1, 5, 8, 9, 10, 17, 17, 20]  # some price values
PRICES = randomIntArray(low=1, ordered=True, length=100, high=2000)
# PRICES_RAND = randomIntArray(low=0, ordered=True)


def CutRod(rod_len: int) -> int:
    if rod_len == 0:
        return 0
    if rod_len == 1:
        return PRICES[0]

    best = 0

    for i in range(1, rod_len + 1):
        price_if_make_cut = CutRod(rod_len - i) + PRICES[i - 1]
        best = max(best, price_if_make_cut)

    return best


def CutRod_DP(max_rod_len: int) -> int:
    dpTable = np.zeros(shape=(max_rod_len + 1), dtype="int")
    """ 
    if rod_len == 0: return 0
    if rod_len == 1: return PRICES[0]
    """
    dpTable[0] = 0
    dpTable[1] = PRICES[0]
    parentPointer = {}
    """ for each missing entry"""
    for rod_len in range(2, max_rod_len + 1):
        best = 0
        bestChoice = 0
        """ This is the loop on line 15"""
        for choice in range(1, rod_len + 1):
            price_if_make_cut = dpTable[rod_len - choice] + PRICES[choice - 1]
            if price_if_make_cut > best:
                best = price_if_make_cut
                bestChoice = choice
        # record choice, this is the i that minimizes CutRod(n-i)
        parentPointer[rod_len] = bestChoice
        dpTable[rod_len] = best

    return dpTable[max_rod_len], parentPointer


def recoverCuts(parentPointers: dict[int, int]):
    curr = len(PRICES)  # start with full rod len
    remainingLength = len(PRICES)
    cuts = []
    while curr in parentPointers:
        cut = parentPointers[curr]
        cuts.append(cut)
        if curr == cut:  # if we cut the entire rod, then we are done, break the loop
            break
        curr = remainingLength - cut
        remainingLength -= cut
    print(f'Profit should match DP result: {sum(map(lambda i: PRICES[i-1], cuts))}')
    return cuts


if __name__ == "__main__":
    # print(PRICES)
    start = time()
    profit, parentPointers = CutRod_DP(len(PRICES))
    end = time()
    print(f"DP: The max profit is: {profit}")
    print(parentPointers)
    print(f"Recovering cuts with parent pointer:")
    print(recoverCuts(parentPointers))
    print(f"Time: {end - start}s")
