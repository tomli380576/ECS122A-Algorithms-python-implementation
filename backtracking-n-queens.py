import numpy as np
from random import randint

EMPTY = 0
OCCUPIED = 1
ChessBoard = np.ndarray


def wontBeAttacked(board: ChessBoard, position_row: int,
                   position_col: int) -> bool:
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            if board[row, col] == OCCUPIED:
                # diagonal
                if abs(position_col - col) == abs(position_row - row):
                    return False
                # vertical or horizontal
                if position_row - row == 0 or position_col - col == 0:
                    return False
    return True


def NQueens(board: ChessBoard, curr_row: int,
            num_solutions: list[int]) -> None:
    if (curr_row == board.shape[0]):
        '''
        Went outside the board, so we found a solution
        record result
        '''
        num_solutions[0] += 1
        return

    for col in range(board[curr_row].shape[0]):
        if wontBeAttacked(board, curr_row, col):
            '''
            make choice
            recursive call
            - subproblem is the modified board
            - state is the current row number
            undo choice, always undo b/c we want all solutions
            '''
            board[curr_row, col] = OCCUPIED
            NQueens(board, curr_row + 1, num_solutions)
            board[curr_row, col] = EMPTY


def NQueens_wrapper(board: ChessBoard, curr_row: int) -> int:
    num_solutions = [0]  # array wrapper to force pass by reference
    NQueens(board, curr_row, num_solutions)
    return num_solutions[0]


if __name__ == '__main__':
    '''
    Gets really slow if n >= 10
    - Answer for N=8 is 92
    - Read more about the math behind this: https://en.wikipedia.org/wiki/Eight_queens_puzzle
    '''
    N = randint(4, 10)
    print(f'Chose: {N} queens')

    empty_board = np.zeros(shape=(N, N), dtype='int')
    result = NQueens_wrapper(empty_board, 0)
    
    print(f'There are {result} possible solutions for a {N}x{N} board.')
