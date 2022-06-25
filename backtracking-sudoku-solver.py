import numpy as np

EMPTY = 0

sample_board = np.array([[2, 3, 0, 4, 1, 5, 0, 6, 8],
                   [0, 8, 0, 2, 3, 6, 5, 1, 9],
                   [1, 6, 0, 9, 8, 7, 2, 3, 4],
                   [3, 1, 7, 0, 9, 4, 0, 2, 5],
                   [4, 5, 8, 1, 2, 0, 6, 9, 7],
                   [9, 2, 6, 0, 5, 8, 3, 0, 1],
                   [0, 0, 0, 5, 0, 0, 1, 0, 2],
                   [0, 0, 0, 8, 4, 2, 9, 0, 3],
                   [5, 9, 2, 3, 7, 1, 4, 8, 6]])


def isSolved(sudoku: np.ndarray) -> bool:
    for row in sudoku:
        if (np.unique(row).shape[0] != 9):
            return False
    for col in sudoku.transpose():
        if (np.unique(col).shape[0] != 9):
            return False
    for y in range(1, 8, 3):
        for x in range(1, 8, 3):
            box = sudoku[y-1:y+2, x-1:x+2]
            if (np.unique(box).shape[0] != 9):
                return False
    return True


def getSudokuChoices(sudoku: np.ndarray, position: tuple[int, int]) -> set[int]:
    y, x = position
    row = sudoku[y]
    col = sudoku.transpose()[x]
    box_y, box_x = (y // 3) * 3 + 1, (x // 3) * 3 + 1
    box = sudoku[box_y-1:box_y+2, box_x-1:box_x+2]

    # Take the choices that satisfy all of them
    choices = (set(range(1, 10)) - set(np.unique(col)))\
        .intersection(set(range(1, 10)) - set(np.unique(box)))\
        .intersection(set(range(1, 10)) - set(np.unique(row)))

    return choices


def sudokuSolver(sudoku: np.ndarray) -> bool:
    if (isSolved(sudoku)):
        return True

    for y, x in np.ndindex(sudoku.shape):
        if (sudoku[y, x] == EMPTY):
            for choice in getSudokuChoices(sudoku, (y, x)):
                sudoku[y, x] = choice
                if (sudokuSolver(sudoku)):
                    return True
                else:
                    sudoku[y, x] = EMPTY
    return False

if __name__ == '__main__':
	sudokuSolver(sample_board)
	print(f'First Solution:\n {sample_board}')