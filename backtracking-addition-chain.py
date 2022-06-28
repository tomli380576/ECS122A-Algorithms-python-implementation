from typing import Union
import math

number = Union[int, float]


def AdditionChain(n: int,
                  curr_chain: list,
                  result_arr: list,
                  rec_level=0) -> number:
    if curr_chain[len(curr_chain) - 1] == n:
        print(f'{curr_chain}, n={n}, r={rec_level}')
        result_arr.clear()
        for elem in curr_chain:
            if elem not in result_arr:
                result_arr.append(elem)
        return 0

    best_len = math.inf

    # ? Reverse order doesn't work for some reason
    for elem1 in curr_chain:
        for elem2 in curr_chain:
            pair_sum = elem1 + elem2
            if pair_sum > curr_chain[len(curr_chain) - 1]\
                    and pair_sum <= n:
                take = AdditionChain(n, curr_chain + [pair_sum], result_arr,
                                     rec_level + 1) + 1
                if take < best_len:
                    best_len = take
    return best_len


if __name__ == '__main__':
    w = []
    AdditionChain(12, [1], result_arr=w)
    print(w)
