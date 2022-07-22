import numpy as np
from random import randint

EMPTY = 0
OCCUPIED = 1


def wontBeAttacked(board: np.ndarray, curr_row: int, position: int) -> bool:
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            if board[row, col] == OCCUPIED:
                # diagonal
                if abs(position - col) == abs(curr_row - row):
                    return False
                # vertical or horizontal
                if curr_row - row == 0 or position - col == 0:
                    return False
    return True


def NQueens(board: np.ndarray, row: int, num_solutions: list[int]) -> None:
    if (row == board.shape[0]):
        '''
        Went outside the board, so we found a solution
        record result
        '''
        num_solutions[0] += 1
        return

    for col in range(board[row].shape[0]):
        if wontBeAttacked(board, row, col):
            '''
            make choice
            recursive call
            - subproblem is the modified board
            - state is the current row number
            undo choice, always undo b/c we want all solutions
            '''
            board[row, col] = OCCUPIED
            NQueens(board, row + 1, num_solutions)
            board[row, col] = EMPTY


def NQueens_wrapper(board: np.ndarray, row: int) -> int:
    num_solutions = [0]  # array wrapper to force pass by reference
    NQueens(board, row, num_solutions)
    return num_solutions[0]


if __name__ == '__main__':
    '''
    Gets really slow if n >= 10
    - Answer for N=8 is 92 
    '''
    N = randint(4, 10)
    empty_board = np.zeros(shape=(N, N), dtype='int')

    print(f'Chose: {N} queens')
    result = NQueens_wrapper(empty_board, 0)
    print(f'There are {result} possible solutions for a {N}x{N} board.')
