from typing import Union
from math import inf


def additionChain(n: int, currChain: list, resultArr: list) -> Union[int, float]:
    """
    If the last choice reached the end
    """
    if currChain[-1] == n:
        """
        Force deep copy
        """
        resultArr.clear()
        for elem in currChain:
            if elem not in resultArr:
                resultArr.append(elem)
        """
        return 0 because dist from n to n is 0
        """
        return 0

    best_len = inf

    # ? Reverse order doesn't work for some reason
    for elem1 in currChain:
        for elem2 in currChain:
            pair_sum = elem1 + elem2
            if pair_sum > currChain[-1] and pair_sum <= n:
                """
                For each pair, if their sum satisfies:
                - greated than previous choice
                - <= n
                Then make choice:
                - state after choice is the new chain
                """
                take = additionChain(n, currChain + [pair_sum], resultArr) + 1
                if take < best_len:
                    best_len = take
    return best_len


if __name__ == "__main__":
    w = []
    """
    The chain always starts with 1
    This gets extremely slow once n > 10
    """
    additionChain(11, [1], resultArr=w)
    print(w)
