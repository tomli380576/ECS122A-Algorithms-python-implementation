from time import time
import numpy as np
from functools import cache


def EditDistance(A: str, B: str, i: int, j: int) -> int:
    if i == -1:
        # +1 offset because i and j are array indices
        return j + 1
    if j == -1:
        return i + 1

    return min(
        EditDistance(A, B, i, j - 1) + 1,  # Insert
        EditDistance(A, B, i - 1, j) + 1,  # Delete
        EditDistance(A, B, i - 1, j - 1) +
        (1 if A[i] != B[j] else 0))  # Replace


@cache
def EditDistance_withCache(A: str, B: str, i: int, j: int) -> int:
    if i == -1:
        return j + 1
    if j == -1:
        return i + 1

    return min(
        EditDistance_withCache(A, B, i, j - 1) + 1,  # Insert
        EditDistance_withCache(A, B, i - 1, j) + 1,  # Delete
        EditDistance_withCache(A, B, i - 1, j - 1) +
        (1 if A[i] != B[j] else 0))  # Replace


def EditDistance_DP(A: str, B: str) -> int:
    # Native Python preallocation:
    #                                  axis 2                     axis 1
    # dpTable = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    dp_table = np.zeros(shape=(len(A) + 1, len(B) + 1), dtype='int')

    for k in range(len(B)):
        dp_table[-1, k] = k + 1  # if i == 0: return j + 1
    for k in range(len(A)):
        dp_table[k, -1] = k + 1  # if j == 0: return i + 1

    # Order of Evaluaion
    # it doesn't really matter which loop goes on the outside
    for i in range(len(A)):
        for j in range(len(B)):
            dp_table[i, j] = min(
                dp_table[i, j - 1] + 1,  # Insert
                dp_table[i - 1, j] + 1,  # Delete
                dp_table[i - 1, j - 1] + (1 if A[i] != B[j] else 0))  # Replace

    return dp_table[len(A) - 1, len(B) - 1]


if __name__ == '__main__':
    A = 'algorithm'
    B = 'altruistic'

    start = time()
    print(
        f'Edit distance from \033[96m{A}\033[0m to \033[96m{B}\033[0m is \033[93m{EditDistance_DP(A, B)}\033[0m'
    )
    end = time()

    print(f'DP: {end - start}s')

    start = time()
    EditDistance_withCache(A, B, len(A) - 1, len(B) - 1)
    end = time()

    print(f'Libray Cache Wrapper: {end - start}s')

    start = time()
    EditDistance(A, B, len(A) - 1, len(B) - 1)
    end = time()
    print(f'Raw Backtracking: {end - start}s')
