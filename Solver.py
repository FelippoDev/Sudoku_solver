import numpy as np
board = [5, 3, 0, 0, 7, 0, 0, 0, 0], \
        [6, 0, 0, 1, 9, 5, 0, 0, 0], \
        [0, 9, 8, 0, 0, 0, 0, 6, 0], \
        [8, 0, 0, 0, 6, 0, 0, 0, 3], \
        [4, 0, 0, 8, 0, 3, 0, 0, 1], \
        [7, 0, 0, 0, 2, 0, 0, 0, 6], \
        [0, 6, 0, 0, 0, 0, 2, 8, 0], \
        [0, 0, 0, 4, 1, 9, 0, 0, 5], \
        [0, 0, 0, 0, 8, 0, 0, 7, 9],


def possible(row, col, n):
    global board
    for i in range(0, 9):
        if board[row][i] == n:
            return False
    for i in range(0, 9):
        if board[i][col] == n:
            return False
    row0 = (row // 3) * 3
    col0 = (col // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if board[row0 + i][col0 + j] == n:
                return False

    return True


def solve():
    global board
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for i in range(1, 10):
                    if possible(x, y, i):
                        board[x][y] = i
                        solve()
                        board[x][y] = 0
                return
    print(np.matrix(board))


solve()
