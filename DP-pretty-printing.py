from math import inf


def DP_PrettyPrint(words: list[str], line_width: int):
    total_cost = [0 for _ in range(len(words) + 1)]
    total_cost[-1] = 0

    line_cost = [[0 for _ in range(len(words) + 1)]
                 for _ in range(len(words) + 1)]
    '''
    Memoize all line costs
    '''
    for i in range(len(words)):
        for j in range(len(words)):
            empty_space = line_width - len(' '.join(words[i:j + 1]))
            if empty_space < 0:
                line_cost[i][j] = inf  #type: ignore
            elif empty_space >= 0 and j == len(words) - 1:
                line_cost[i][j] = 0
            else:
                line_cost[i][j] = empty_space**3
    '''
    main recurrence
    '''
    # This simulates the function call PrettyPrint(..., curr_word_idx)
    # Apply order of evaulation here. 
    # curr_word_idx needs min from 1 to curr_word_idx - 1
    for last_word_idx in (range(0, len(words))):
        best_cost = inf
        # This is the actual for loop inside the PrettyPrint() function
        for break_idx in reversed(range(0, last_word_idx + 1)):
            break_cost = total_cost[break_idx -
                                    1] + line_cost[break_idx][last_word_idx]
            if break_cost < best_cost:
                best_cost = break_cost

        total_cost[last_word_idx] = best_cost  #type:ignore

    return total_cost[len(words) - 1]


if __name__ == '__main__':
    text1 = 'Geeks for Geeks presents word wrap problem'
    text2 = 'aaa bb cc ddddd'
    text3 = 'cat is an animal'
    text4 = 'This is an example of text justification'
    words = text4.split(' ')
    line_width = 15

    cost = DP_PrettyPrint(words, line_width)

    print(words)
    print(f'Total cost: {cost}')