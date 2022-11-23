from math import inf


def PrettyPrint_DP(words: list[str], lineWidth: int):
    totalCost = [0 for _ in range(len(words) + 1)]
    totalCost[-1] = 0
    # Memoize all the Extras(i, j) values
    extras = [[0 for _ in range(len(words) + 1)] for _ in range(len(words) + 1)]
    for i in range(len(words)):
        for j in range(i, len(words)):
            if j == i:  # base case
                extras[i][j] = lineWidth - len(words[i])
                continue
            extras[i][j] = extras[i][j - 1] - 1 - len(words[j])
    """
    Memoize PrettyPrint(..., curr_word_idx)
    Apply order of evaulation here.
    lastWordIndex needs min from 1 to lastWordIndex - 1
    """
    breaks = []
    for lastWordIndex in range(0, len(words)):
        bestCost = inf
        bestBreak = None
        # This is the actual for loop inside the backtracking PrettyPrint() function
        for breakIndex in range(0, lastWordIndex + 1):
            # Simulate the LineCost() function, same logic just slightly rearranged
            lineCost = inf
            # Use the memoized result of Extras(breakIndex, lastWordIndex)
            emptySpaces = extras[breakIndex][lastWordIndex]
            if emptySpaces >= 0:
                # last line is free
                if lastWordIndex == len(words) - 1:
                    lineCost = 0
                else:
                    lineCost = emptySpaces**3
            # Simulates the recursive call PrettyPrint(breakIndex - 1) + LineCost()
            breakCost = totalCost[breakIndex - 1] + lineCost
            # bestCost = min(bestCost, breakCost)
            if breakCost < bestCost:
                bestCost = breakCost
                bestBreak = breakIndex
        totalCost[lastWordIndex] = bestCost
        breaks.append(bestBreak)

    print(breaks)
    return totalCost[len(words) - 1]


if __name__ == "__main__":
    text1 = "The cat ran very slowly to the school"
    text2 = "aaa bb cc ddddd"
    text3 = "cat is an animal"
    text4 = "This is an example of text justification"
    words = text1.split(" ")
    lineWidth = 15

    cost = PrettyPrint_DP(words, lineWidth)

    print(words)
    print(f"Total cost: {cost}")
