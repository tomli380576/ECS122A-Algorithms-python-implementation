from typing import Union
from math import inf


def AdditionChain(n: int, curr_chain: list,
                  result_arr: list) -> Union[int, float]:
    '''
    If the last choice reached the end
    '''
    if curr_chain[-1] == n:
        '''
        Force deep copy
        '''
        result_arr.clear()
        for elem in curr_chain:
            if elem not in result_arr:
                result_arr.append(elem)
        '''
        return 0 because dist from n to n is 0
        '''
        return 0

    best_len = inf

    # ? Reverse order doesn't work for some reason
    for elem1 in curr_chain:
        for elem2 in curr_chain:
            pair_sum = elem1 + elem2
            if pair_sum > curr_chain[-1] and pair_sum <= n:
                '''
                For each pair, if their sum satisfies:
                - greated than previous choice
                - <= n
                Then make choice:
                - state after choice is the new chain
                '''
                take = AdditionChain(n, curr_chain + [pair_sum],
                                     result_arr) + 1
                if take < best_len:
                    best_len = take
    return best_len


if __name__ == '__main__':
    w = []
    '''
    The chain always starts with 1
    This gets extremely slow once n > 10
    '''
    AdditionChain(11, [1], result_arr=w)
    print(w)
