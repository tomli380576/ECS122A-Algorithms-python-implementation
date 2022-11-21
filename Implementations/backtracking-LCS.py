from random_inputs import randomString
from random import randint


# returns length
def LCS_length(X: str, Y: str, i: int, j: int) -> int:
    if i == len(X) or j == len(Y):
        return 0
    if X[i] == Y[j]:
        return LCS_length(X, Y, i + 1, j + 1) + 1
    else:
        return max(LCS_length(X, Y, i + 1, j), LCS_length(X, Y, i, j + 1))


# returns sequence
def LCS_seq(X: str, Y: str, x_idx: int, y_idx: int) -> str:
    if x_idx == len(X) or y_idx == len(Y):
        return ""
    if X[x_idx] == Y[y_idx]:
        return X[x_idx] + LCS_seq(X, Y, x_idx + 1, y_idx + 1)
    else:
        # skip the currnt character in x by x_idx + 1
        skip_x = LCS_seq(X, Y, x_idx + 1, y_idx)
        skip_y = LCS_seq(X, Y, x_idx, y_idx + 1)
        if len(skip_x) > len(skip_y):
            return skip_x
        else:
            return skip_y


if __name__ == "__main__":
    """
    Gets really slow if the strings are longer than 20 characters b/c O(2^n) runtime
    """
    X = randomString(length=randint(5, 20)).upper()
    Y = randomString(length=randint(5, 20)).upper()
    print(
        f"The LCS between '{X}' and '{Y}' is '{LCS_seq(X, Y, 0, 0)}' with length {LCS_length(X, Y, i=0, j=0)}"
    )
