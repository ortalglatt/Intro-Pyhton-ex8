import ex8
import math


def check_solution(board):
    col_lst = col_list(board)
    square_len = int(math.sqrt(len(board)))

    for num in range(1, len(board) + 1):
        for row in range(len(board)):
            assert board[row].count(num) == 1
        for col in range(len(col_lst)):
            assert col_lst[col].count(num) == 1
        for row in range(square_len):
            for col in range(square_len):
                small_board = square_board(board, row, col)
                assert small_board.count(num) == 1


def col_list(board):
    col_lst = []
    for col in range(len(board)):
        col_sublist = []
        for row in range(len(board)):
            col_sublist.append(board[row][col])
        col_lst.append(col_sublist)
    return col_lst


def square_board(board, row, col):
    square_len = int(math.sqrt(len(board)))
    square_board = list()
    start_row = square_len * (row // square_len)
    start_col = square_len * (col // square_len)
    for row in board[start_row: start_row + square_len]:
        square_board += (row[start_col: start_col + square_len])
    return square_board


def did_not_change_at_all(start_board, final_board):
    assert start_board == final_board


def did_not_change_start_numbers(start_board, final_board):
    for row in range(len(start_board)):
        for col in range(len(start_board)):
            if start_board[row][col] != 0:
                assert start_board[row][col] == final_board[row][col]


board = [[4, 0, 0, 0],
                                  [0, 2, 4, 3],
                                  [3, 0, 0, 0],
                                  [2, 0, 3, 0]]
ex8.solve_sudoku(board)
check_solution(board)