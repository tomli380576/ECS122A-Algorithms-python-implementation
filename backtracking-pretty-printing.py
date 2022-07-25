from math import inf


def LineCost(words, line_width, i, j):
    '''
    i, j are valid indices, inclusive
    '''
    extras = line_width - len(' '.join(words[i:j + 1]))
    if extras < 0:
        return inf
    # '''
    # Depends on the problem,
    # enable this if the last line is free
    # '''
    if extras >= 0 and j == len(words) - 1:
        return 0
    else:
        return extras**3


def PrettyPrint(WORDS, LINE_WIDTH, last_word_idx) -> tuple[int, list]:
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
    words = text4.split(' ')

    line_width = 15

    cost, breaks = PrettyPrint(words, line_width, len(words) - 1)

    for i in breaks:
        if i != 0:
            words[i] = '\n' + words[i]
    print(f'Cost: {cost}')
    print(' '.join(words))