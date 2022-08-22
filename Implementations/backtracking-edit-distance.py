from random_inputs import randomString
from random import randint


def EditDistance(A: str, B: str, i: int, j: int) -> int:
    '''
    +1 offset because i and j are array indices
    '''
    if i == -1:
        return j + 1
    if j == -1:
        return i + 1

    return min(
        EditDistance(A, B, i, j - 1) + 1,  # Insert
        EditDistance(A, B, i - 1, j) + 1,  # Delete
        EditDistance(A, B, i - 1, j - 1) +
        (1 if A[i] != B[j] else 0))  # Replace


if __name__ == '__main__':
    use_random_inputs = bool(input('Random? (y/n) ').lower() == 'y')
    print('Using sample inputs.')

    A = 'algorithm'
    B = 'altruistic'

    if use_random_inputs:
        A = randomString(length=randint(5, 10))
        B = randomString(length=randint(5, 10))
        print(f'A={A}, B={B}')
    print(
        f'Edit distance from \033[95m{A}\033[0m to \033[95m{B}\033[0m is: {EditDistance(A, B, len(A) - 1, len(B) - 1)}'
    )
