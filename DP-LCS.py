import numpy as np
from random_inputs import randomString
from random import randint


def LCS_DP_Length(X: str, Y: str) -> int:
    dpTable = np.zeros(shape=(len(X) + 1, len(Y) + 1), dtype='int')

    for i in range(len(Y)):
        dpTable[len(X), i] = 0  # if x_idx == len(X)
    for i in range(len(X)):
        dpTable[i, len(Y)] = 0  # if y_idx == len(Y)

    for i in reversed(range(len(X))):
        for j in reversed(range(len(Y))):
            if X[i] == Y[j]:
                dpTable[i, j] = dpTable[i + 1, j + 1] + 1
            else:
                dpTable[i, j] = max(dpTable[i + 1, j],
                                            dpTable[i, j + 1])
    return dpTable[0, 0]


def LCS_DP_Sequence(X: str, Y: str) -> str:
    '''
    do not use dtype = 'str' here
    numpy string and python native strings are different
    '''
    dp_table: np.ndarray = np.zeros(shape=(len(X) + 1, len(Y) + 1),
                                   dtype=object)
    '''Fill in the base cases'''
    for i in range(len(Y)):
        dp_table[len(X), i] = ''  # if x_idx == len(X)
    for i in range(len(X)):
        dp_table[i, len(Y)] = ''  # if y_idx == len(Y)
    '''
    Order of evaluation
    Reverse the scanning direction (check notion) to get the 122 A version
    '''
    for i in reversed(range(len(X))):
        for j in reversed(range(len(Y))):
            if X[i] == Y[j]:
                dp_table[i,
                        j] = X[i] + dp_table[i + 1, j + 1]
            else:
                skip_x = len(dp_table[i + 1, j])
                skip_y = len(dp_table[i, j + 1])
                if skip_x > skip_y:
                    # LCS_seq(X, Y, x_idx + 1, y_idx)
                    dp_table[i, j] = dp_table[i + 1, j]
                else:
                    # LCS_seq(X, Y, x_idx, y_idx + 1)
                    dp_table[i, j] = dp_table[i, j + 1]
    # simulate initial call
    return dp_table[0, 0]


if __name__ == '__main__':
    X = randomString(length=randint(5, 50))
    Y = randomString(length=randint(5, 50))

    print(
        f'X = {X} \nY = {Y}\nLCS is: \'{LCS_DP_Sequence(X, Y)}\' with length = {LCS_DP_Length(X, Y)}'
    )
