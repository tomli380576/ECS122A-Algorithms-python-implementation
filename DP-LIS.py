import math
import numpy as np


def LIS_index_based(A: list, i: int, j: int) -> int:
    if j >= len(A):
        return 0
    elif A[i] >= A[j]:
        return LIS_index_based(A, i, j + 1)
    else:
        take = LIS_index_based(A, j, j + 1) + 1
        leave = LIS_index_based(A, i, j + 1)
        return max(take, leave)


def LIS_DP(A_original: list) -> int:
    A = [-math.inf] + A_original
    N = len(A)
    # N+1 for the number of columns becasue we need j = N as the base case
    dp_table: np.ndarray = np.zeros(shape=(N, N + 1), dtype='int')
    result = []
    # initialize base cases
    for i in range(len(A)):
        # this corresponds to `if j >= len(A)`
        # needed for all the i's
        dp_table[i, N] = 0

    for j in reversed(range(1, N)):
        for i in range(N - 1):
            if A[i] >= A[j]:
                dp_table[i, j] = dp_table[i, j + 1]
            else:
                take = dp_table[j, j + 1] + 1
                leave = dp_table[i, j + 1]
                dp_table[i, j] = max(take, leave)
                if take > leave:
                    if (dp_table[i, j]) > len(result):
                        result.append(A[j])
                    # We want to directly replace the element in the sequence
                    # Not always appending to the back
                    else:
                        result[dp_table[i, j] - 1] = A[j]
    result.reverse()
    print(f'Sequence Contents: {result}')
    # This corresponds to the initial call LIS(i=0, j=1)
    return dp_table[0, 1]


if __name__ == '__main__':
    sample_set = [
        3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6
    ]
    print(f'Index version: {LIS_index_based([-math.inf] + sample_set, 0,1)}'
          )  # type: ignore
    print(f'DP version: {LIS_DP(sample_set)}')
