import numpy as np

EMPTY = 0


def IsSolved(sudoku: np.ndarray) -> bool:
    for row in sudoku:
        if (np.unique(row).shape[0] != 9):
            '''
            If there are repeating numbers
            '''
            return False
    for col in sudoku.transpose():
        if (np.unique(col).shape[0] != 9):
            return False
    for y in range(1, 8, 3):
        for x in range(1, 8, 3):
            box = sudoku[y - 1:y + 2, x - 1:x + 2]
            if (np.unique(box).shape[0] != 9):
                return False
    return True


def GetSudokuChoices(sudoku: np.ndarray, position: tuple[int,
                                                         int]) -> set[int]:
    y, x = position
    row = sudoku[y]
    col = sudoku.transpose()[x]
    box_y, box_x = (y // 3) * 3 + 1, (x // 3) * 3 + 1
    box = sudoku[box_y - 1:box_y + 2, box_x - 1:box_x + 2]

    # Take the choices that satisfy all of them
    choices = (set(range(1, 10)) - set(np.unique(col)))\
        .intersection(set(range(1, 10)) - set(np.unique(box)))\
        .intersection(set(range(1, 10)) - set(np.unique(row)))

    return choices


def SudokuSolver(sudoku: np.ndarray) -> bool:
    if IsSolved(sudoku):
        return True

    for y, x in np.ndindex(sudoku.shape):
        if (sudoku[y, x] == EMPTY):
            for choice in GetSudokuChoices(sudoku, (y, x)):
                # try to make a choice
                sudoku[y, x] = choice
                # if the recursion tells us that it worked, return true
                if SudokuSolver(sudoku):
                    return True
                # otherwise undo the chocie
                else:
                    sudoku[y, x] = EMPTY
    # we tried all the valid choices, nothing worked
    return False


if __name__ == '__main__':

    sample_board = np.array([[2, 3, 0, 4, 1, 5, 0, 6, 8],
                             [0, 8, 0, 2, 3, 6, 5, 1, 9],
                             [1, 6, 0, 9, 8, 7, 2, 3, 4],
                             [3, 1, 7, 0, 9, 4, 0, 2, 5],
                             [4, 5, 8, 1, 2, 0, 6, 9, 7],
                             [9, 2, 6, 0, 5, 8, 3, 0, 1],
                             [0, 0, 0, 5, 0, 0, 1, 0, 2],
                             [0, 0, 0, 8, 4, 2, 9, 0, 3],
                             [5, 9, 2, 3, 7, 1, 4, 8, 6]])

    SudokuSolver(sample_board)
    print(f'First Solution:\n {sample_board}')
