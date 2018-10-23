import numpy as np

def display_board(board):
    for row in board:
        print(row)
    print(20*'*')


def matrix_transpose(matrix):
    return list(zip(*matrix))


def remove_fixed_from_rows(board, init=False):
    result = []
    for row in board:
        res_row = []
        for el in row:
            if isinstance(el, int) and el != 0:
                res_row.append(el)
            else:
                if init:
                    res_row.append(set(range(1, 10)).difference(set(row)))
                else:
                    new = el.difference(set([el for el in row if isinstance(el, int)]))
                    if len(new) == 1:
                        res_row.append(new.pop())
                    else:
                        res_row.append(new)
        result.append(res_row)
    return result


def rem(board, begin, end):
    result = []
    for row in board[begin:end]:
        res_row = []
        for el in row[begin:end]:
            if isinstance(el, int) and el != 0:
                res_row.append(el)
            else:
                new = el.difference(set([el for el in row if isinstance(el, int)]))
                if len(new) == 1:
                    res_row.append(new.pop())
                else:
                    res_row.append(new)

        result.append(res_row)
    return result


def rem2(board, begin, end):
    t = []
    temp = []
    for row in board[begin:end]:
        t += row[begin:end]
    for el in t:
        if isinstance(el, int):
            temp.append(el)
        else:
            new = el.difference(set([e for e in t if isinstance(e, int)]))
            if len(new) == 1:
                temp.append(new.pop())
            else:
                temp.append(new)
    return [temp[0:3], temp[3:6], temp[6:]]


sudoku = [
    [7, 6, 0, 5, 0, 0, 0, 0, 4],
    [1, 0, 0, 3, 0, 7, 8, 0, 0],
    [0, 8, 0, 0, 0, 6, 3, 0, 9],
    [0, 7, 0, 0, 1, 0, 2, 3, 0],
    [3, 0, 0, 0, 8, 0, 0, 0, 7],
    [0, 5, 6, 0, 7, 3, 0, 8, 0],
    [5, 0, 1, 9, 0, 0, 0, 4, 0],
    [0, 0, 9, 7, 0, 1, 0, 0, 2],
    [6, 0, 0, 0, 0, 4, 0, 1, 3],
     ]
board = remove_fixed_from_rows(sudoku, init=True)
display_board(board)
board = matrix_transpose(remove_fixed_from_rows(matrix_transpose(board)))
display_board(board)

board = np.transpose(board)
