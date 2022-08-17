from typing import Union
from math import inf


def LineCost(WORDS: list[str], LINE_WIDTH: int, i: int,
             j: int) -> Union[float, int]:
    '''
    i, j are valid indices, inclusive
    '''
    extras = LINE_WIDTH - len(' '.join(WORDS[i:j + 1]))
    if extras < 0:
        return inf
    if extras >= 0 and j == len(WORDS) - 1:
        '''
        Depends on the problem,
        enable this if the last line is free
        '''
        return 0
    else:
        return extras**3


def PrettyPrint(WORDS: list[str], LINE_WIDTH: int,
                last_word_idx: int) -> tuple[int, list]:
    if last_word_idx == -1:
        return 0, []

    best_cost = inf
    best_breaks = []

    for break_idx in range(0, last_word_idx + 1):
        break_cost, breaks = PrettyPrint(WORDS, LINE_WIDTH, break_idx - 1)
        break_cost += LineCost(WORDS, LINE_WIDTH, break_idx, last_word_idx)

        if break_cost < best_cost:
            best_cost = break_cost
            best_breaks = breaks + [break_idx]

    return best_cost, best_breaks  # type: ignore


if __name__ == '__main__':
    text1 = 'Geeks for Geeks presents word wrap problem'
    text2 = 'aaa bb cc ddddd'
    text3 = 'cat is an animal'
    text4 = 'This is an example of text justification'

    words = text3.split(' ')
    line_width = 6

    cost, breaks = PrettyPrint(words, line_width, len(words) - 1)

    print(f'Cost = {cost}, printing justified words:\n----')

    for i in breaks:
        if i != 0:
            words[i] = '\n' + words[i]

    print(' '.join(words))
