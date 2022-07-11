import numpy as np


def LCS_DP_Length(X: str, Y: str) -> int:
    dpTable = np.zeros(shape=(len(X) + 1, len(Y) + 1), dtype='int')
    # Fill in the base cases
    for i in range(len(Y)):
        dpTable[len(X), i] = 0  # if x_idx == len(X)
    for i in range(len(X)):
        dpTable[i, len(Y)] = 0  # if y_idx == len(Y)

    for x_idx in reversed(range(len(X))):
        for y_idx in reversed(range(len(Y))):
            if X[x_idx] == Y[y_idx]:
                dpTable[x_idx, y_idx] = dpTable[x_idx + 1, y_idx + 1] + 1
            else:
                dpTable[x_idx, y_idx] = max(dpTable[x_idx + 1, y_idx],
                                            dpTable[x_idx, y_idx + 1])
    return dpTable[0, 0]


def LCS_DP_Sequnce(X: str, Y: str) -> str:
    # do not use dtype = 'str' here, numpy string and python native strings are different
    dpTable: np.ndarray = np.zeros(shape=(len(X) + 1, len(Y) + 1),
                                   dtype=np.object_)

    # Fill in the base cases
    for i in range(len(Y)):
        dpTable[len(X), i] = ''  # if x_idx == len(X)
    for i in range(len(X)):
        dpTable[i, len(Y)] = ''  # if y_idx == len(Y)

    # Order of evaluation
    for x_idx in reversed(range(len(X))):
        for y_idx in reversed(range(len(Y))):
            if X[x_idx] == Y[y_idx]:
                dpTable[x_idx,
                        y_idx] = X[x_idx] + dpTable[x_idx + 1, y_idx + 1]
            else:
                skip_x = len(dpTable[x_idx + 1, y_idx])
                skip_y = len(dpTable[x_idx, y_idx + 1])
                if skip_x > skip_y:
                    # LCS_seq(X, Y, x_idx + 1, y_idx) call
                    dpTable[x_idx, y_idx] = dpTable[x_idx + 1, y_idx]
                else:
                    # LCS_seq(X, Y, x_idx, y_idx + 1) call
                    dpTable[x_idx, y_idx] = dpTable[x_idx, y_idx + 1]
    # simulate initial call
    return dpTable[0, 0]


if __name__ == '__main__':
    X: str = 'DUTC'
    Y: str = 'DCUT'
    print(
        f'The LCS between {X} and {Y} is {LCS_DP_Sequnce(X, Y)} with length = {LCS_DP_Length(X, Y)}'
    )
