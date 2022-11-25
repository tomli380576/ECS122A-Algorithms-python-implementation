import numpy as np
from random_inputs import randomString
from random import randint


def LCS_DP_Length(X: str, Y: str) -> tuple[int, dict]:
    """
    To get a better understanding,
    comapre the backtracking version with this DP version
    and see how things line up
    """
    dp_table = np.zeros(shape=(len(X) + 1, len(Y) + 1), dtype="int")

    for i in range(len(Y)):
        dp_table[len(X), i] = 0  # if x_idx == len(X)
    for i in range(len(X)):
        dp_table[i, len(Y)] = 0  # if y_idx == len(Y)

    parent = {}  # stores the parent pointers to recover the actual matches
    for i in reversed(range(len(X))):
        for j in reversed(range(len(Y))):
            if X[i] == Y[j]:
                dp_table[i, j] = dp_table[i + 1, j + 1] + 1
                parent[i, j] = (i + 1, j + 1)  # record choice
            elif dp_table[i + 1, j] > dp_table[i, j + 1]:
                dp_table[i, j] = dp_table[i + 1, j]
                parent[i, j] = (i + 1, j)
            else:
                dp_table[i, j] = dp_table[i, j + 1]
                parent[i, j] = (i, j + 1)

    return dp_table[0, 0], parent


def LCS_DP_Flipped(X: str, Y: str) -> int:
    """
    122A version with reversed order of evaluation
    """
    dp_table = np.zeros(shape=(len(X) + 1, len(Y) + 1), dtype="int")
    """
    Change the base cases as well when we flip order of evaulation
    """
    for i in range(len(Y)):
        dp_table[-1, i] = 0  # if x_idx == -1
    for i in range(len(X)):
        dp_table[i, -1] = 0  # if y_idx == -1

    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i] == Y[j]:
                dp_table[i, j] = dp_table[i - 1, j - 1] + 1
            else:
                dp_table[i, j] = max(dp_table[i - 1, j], dp_table[i, j - 1])

    return dp_table[len(X) - 1, len(Y) - 1]


def LCS_DP_Sequence(X: str, Y: str) -> str:
    """
    Do not use dtype='str' here
    numpy string and python native strings are different
    """
    dp_table: np.ndarray = np.zeros(shape=(len(X) + 1, len(Y) + 1), dtype=np.object_)
    """
    Fill in the base cases
    """
    for i in range(len(Y)):
        dp_table[len(X), i] = ""  # if x_idx == len(X)
    for i in range(len(X)):
        dp_table[i, len(Y)] = ""  # if y_idx == len(Y)
    """
    Order of evaluation
    Reverse the scanning direction (check notion) to get the 122A version
    """
    for i in reversed(range(len(X))):
        for j in reversed(range(len(Y))):
            if X[i] == Y[j]:
                dp_table[i, j] = X[i] + dp_table[i + 1, j + 1]
            else:
                skip_x = len(dp_table[i + 1, j])
                skip_y = len(dp_table[i, j + 1])
                if skip_x > skip_y:
                    """LCS_seq(x_idx + 1, y_idx)"""
                    dp_table[i, j] = dp_table[i + 1, j]
                else:
                    """LCS_seq(x_idx + 1, y_idx + 1)"""
                    dp_table[i, j] = dp_table[i, j + 1]
    # simulate initial call
    return dp_table[0, 0]


def recoverMatches(
    X: str,
    Y: str,
    parentPointer: dict[tuple[int, int], tuple[int, int]],
    backwards: bool,
) -> tuple[list[int], list[int]]:
    curr = (len(X), len(Y)) if backwards else (0, 0)
    matchIdxX = []
    matchIdxY = []
    while curr in parentPointer:
        i, j = curr
        # curr will be all possible index combinations,
        # so we need to check if curr is a match
        # or if curr is just an intermedidate step
        if X[i] == Y[j]:
            matchIdxX.append(i)
            matchIdxY.append(j)
        curr = parentPointer[curr]
    return matchIdxX, matchIdxY


if __name__ == "__main__":
    X = randomString(length=randint(5, 50))
    Y = randomString(length=randint(5, 50))
    # X = "DUCT"
    # Y = "DUTC"

    print(
        f"X = {X} \nY = {Y}\nLCS is: '{LCS_DP_Sequence(X, Y)}' with length = {LCS_DP_Flipped(X, Y)}"
    )

    length, parentPointers = LCS_DP_Length(X, Y)
    matchIdxX, matchIdxY = recoverMatches(X, Y, parentPointers, False)

    print("==> Recovering matches with parentPointer")
    print(f"Indices {matchIdxX} in X matches with indices {matchIdxY} in Y")
    print(
        f"Match index arrays should also have the same length: {len(matchIdxX)} = {len(matchIdxY)}"
    )
    print("==> Reconstructing LCS with the match indices")
    matchCharsX: list[str] = []
    matchCharsY: list[str] = []
    for i, j in zip(matchIdxX, matchIdxY):
        matchCharsX.append(X[i])
        matchCharsY.append(Y[j])
    print(f"The LCS string should also macth the output above")
    print(f"{''.join(matchCharsX)} == {''.join(matchCharsY)}")
