from time import time
import numpy as np


def EditDistance(A: str, B: str, i: int, j: int) -> int:
    if i == -1:
        # +1 offset because i and j are array indices
        return j + 1
    if j == -1:
        return i + 1

    return min(
        EditDistance(A, B, i, j - 1) + 1,
        EditDistance(A, B, i - 1, j) + 1,
        EditDistance(A, B, i - 1, j - 1) + (1 if A[i] != B[j] else 0))


def EditDistance_DP(A: str, B: str) -> int:
    dpTable = np.zeros(shape=(len(A) + 1, len(B) + 1), dtype='int')
    
    for k in range(len(B)):
        dpTable[-1, k] = k + 1  # if i == 0: return j + 1
    for k in range(len(A)):
        dpTable[k, -1] = k + 1  # if j == 0: return i + 1

    # Order of Evaluaion
    # it doesn't really matter which loop goes on the outside
    for i in range(len(A)):
        for j in range(len(B)):
            dpTable[i, j] = min(
                dpTable[i, j - 1] + 1, dpTable[i - 1, j] + 1,
                dpTable[i - 1, j - 1] + (1 if A[i] != B[j] else 0))
    return dpTable[len(A) - 1, len(B) - 1]


if __name__ == '__main__':
    A = 'ALGORITHM'
    B = 'ALTRUISTIC'

    start = time()
    print(f'Edit distance from {A} to {B} is {EditDistance(A, B, len(A) - 1, len(B) - 1)}')
    end = time()

    start2 = time()
    print(f'Edit distance from {A} to {B} is {EditDistance_DP(A, B)}')
    end2 = time()

    print(f'Backtracking: {end-start}s, DP: {end2 - start2}s')