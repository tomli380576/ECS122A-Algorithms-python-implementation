from math import inf


def PrettyPrint_DP(words: list[str], line_width: int):
    total_cost = [0 for _ in range(len(words) + 1)]
    total_cost[-1] = 0
    '''
    Memoize all the Extras(i, j) values
    '''
    extras = [[0 for _ in range(len(words) + 1)]
              for _ in range(len(words) + 1)]

    for i in range(len(words)):
        for j in range(i, len(words)):
            if j == i:  # base case
                extras[i][j] = line_width - len(words[i])
                continue
            extras[i][j] = extras[i][j - 1] - 1 - len(words[j])
    '''
    Memoize PrettyPrint(..., curr_word_idx)
    Apply order of evaulation here.
    curr_word_idx needs min from 1 to curr_word_idx - 1
    '''
    for last_word_idx in range(0, len(words)):
        best_cost = inf
        # This is the actual for loop inside the backtracking PrettyPrint() function
        for break_idx in range(0, last_word_idx + 1):
            '''
            Simulate the LineCost() function, same logic just slightly rearranged
            '''
            line_cost = inf
            empty_spaces = extras[break_idx][last_word_idx]
            if empty_spaces >= 0:
                if last_word_idx == len(words) - 1:
                    line_cost = 0
                else:
                    line_cost = empty_spaces**3
            '''
            Simulate the recursive call PrettyPrint(break_idx - 1)
            '''
            break_cost = total_cost[break_idx - 1] + line_cost
            best_cost = min(best_cost, break_cost)

        total_cost[last_word_idx] = best_cost  # type: ignore

    return total_cost[len(words) - 1]


if __name__ == '__main__':
    text1 = 'Geeks for Geeks presents word wrap problem'
    text2 = 'aaa bb cc ddddd'
    text3 = 'cat is an animal'
    text4 = 'This is an example of text justification'
    words = text1.split(' ')
    line_width = 15

    cost = PrettyPrint_DP(words, line_width)

    print(words)
    print(f'Total cost: {cost}')