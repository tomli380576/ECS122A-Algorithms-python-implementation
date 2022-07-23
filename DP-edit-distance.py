from time import time
from functools import cache
from random_inputs import randomString
from random import randint

@cache
def EditDistance_withCache(A: str, B: str, i: int, j: int) -> int:
    if i == -1:
        return j + 1
    if j == -1:
        return i + 1

    return min(
        EditDistance_withCache(A, B, i, j - 1) + 1,  # Insert
        EditDistance_withCache(A, B, i - 1, j) + 1,  # Delete
        EditDistance_withCache(A, B, i - 1, j - 1) +
        (1 if A[i] != B[j] else 0))  # Replace


def EditDistance_DP(A: str, B: str) -> int:
    dp_table = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

    for k in range(len(B)):
        dp_table[-1][k] = k + 1  # if i == 0: return j + 1
    for k in range(len(A)):
        dp_table[k][-1] = k + 1  # if j == 0: return i + 1
    '''
    Order of Evaluaion
    It doesn't really matter which loop goes on the outside
    '''
    for i in range(len(A)):
        for j in range(len(B)):
            insert = dp_table[i][j - 1] + 1
            delete = dp_table[i - 1][j] + 1
            replace = dp_table[i - 1][j - 1] + (1 if A[i] != B[j] else 0)
            dp_table[i][j] = min(insert, delete, replace)  # Replace

    return dp_table[len(A) - 1][len(B) - 1]


def EditDistance_DP_LessSpace(A: str, B: str) -> int:
    '''
    Refer to the graphical table to see the literal arrays
    Indexing is a bit different from regular DP
    '''
    dp_array1 = [i for i in range(len(B) + 1)]
    dp_array2 = [0 for _ in range(len(B) + 1)]
    '''
    Reverse nesting order also works here
    Just make sure to change the array size to the length of the other string
    '''
    for i in range(1, len(A) + 1):
        for j in range(len(B) + 1):
            if j == 0:
                dp_array1[j] = i - 1
                dp_array2[j] = i
                continue
            ''' 
            accessing dp_array1 simulates the
            dp_table[i - 1, ...] from the original DP solution
            '''
            insert = dp_array2[j - 1] + 1
            delete = dp_array1[j] + 1
            replace = dp_array1[j - 1] + (1 if A[i - 1] != B[j - 1] else 0)

            dp_array2[j] = min(insert, delete, replace)
        '''
        Maybe a slight overhead here compared to regular DP
        We have to copy over the numbers from arr2 to arr1
        If we write this in C++,
        we can use pointers to define which array is dp_array1
        and just write over it
        '''
        dp_array1 = dp_array2
        dp_array2 = [0 for _ in range(len(B) + 1)]

    return dp_array1[len(B)]


if __name__ == '__main__':
    use_random_inputs = True

    A = 'algorithm'
    B = 'altruistic'

    if use_random_inputs:
        A = randomString(length=randint(200, 2000))
        B = randomString(length=randint(200, 2000))

    start = time() * 1000
    edit_dist = EditDistance_DP(A, B)
    end = time() * 1000
    '''
    The weird escape sequences are command line colors
    '''
    print(
        f'Edit distance from \033[95m{A}\033[0m to \033[95m{B}\033[0m is\033[93m {edit_dist}\033[0m'
    )
    print(f'DP: {format(end-start, ".3f")} ms')

    start = time() * 1000
    res = EditDistance_DP_LessSpace(A, B)
    end = time() * 1000
    print(f'Less space DP: {format(end-start, ".3f")} ms')
    '''
    Has to stop here because recursion takes way too long
    The library one will reach max recursion depth
    '''
    if use_random_inputs: exit()

    start = time() * 1000
    res = EditDistance_withCache(A, B, len(A) - 1, len(B) - 1)
    end = time() * 1000
    print(f'Libray Cache Wrapper: {format(end-start, ".3f")} ms')
