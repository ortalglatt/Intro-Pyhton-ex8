import math

ROW = 0
COL = 1
LAST = -1

# Part A


def solve_sudoku(board, start_num=1, start_row=0):
    """This recursive function gets a board - list of lists of numbers, number
    - at the beginning, default value of 1, and a row - at the beginning,
    default value of 0.
    If this sudoku is solvable, the function will fill the '0' cells with the
    right numbers, and return True. If the sudoku isn't solvable, the function
    will return False and the sudoku board will not change."""
    if num_counter(board, 0) == 0:
        return True
    for num in range(start_num, len(board) + 1):
        if num_counter(board, num) == len(board):
            start_row = 0
            continue
        for row in range(start_row, len(board)):
            for col in range(len(board)):
                if not legal_place(board, num, (row, col)):
                    continue
                board[row][col] = num
                if solve_sudoku(board, num, row + 1):
                    return True
                board[row][col] = 0
        return False


def num_counter(board, num):
    """This function gets a sudoku board and a number, and return the number of
    times that this number appears in the board."""
    counter = 0
    for row in board:
        counter += row.count(num)
    return counter


def legal_place(board, num, point):
    """This function gets a board, a number and a point - tuple of a row and a
    column. It checks if the this cell of the board can be fill with the
    number, by checking if the number appears already in the point row, in the
    point column and in the point small square. If that place is legal for this
    number, the function will return True. else, it will return False."""
    row = point[ROW]
    col = point[COL]
    if board[row][col] != 0:
        return False
    elif num in board[row] or num in square_board(board, row, col):
        return False
    else:
        for i in range(len(board)):
            if i != row and board[i][col] == num:
                return False
    return True


def square_board(board, row, col):
    """This function gets a board, a row and a column, and return a list of the
    numbers in the small square of the point (row, col)."""
    square_len = int(math.sqrt(len(board)))
    square_board = list()
    start_row = square_len * (row // square_len)
    start_col = square_len * (col // square_len)
    for row in board[start_row: start_row + square_len]:
        square_board += (row[start_col: start_col + square_len])
    return square_board


# Part B


# Function number 1
def print_k_subsets(n, k):
    """This function gets two numbers - 'n' and 'k', and prints all the k size
    subsets with the numbers from 0 to n-1, when every number in the subset, is
    bigger then the previous number"""
    if k == 0:
        print([])
        return
    if n == 0:
        return
    else:
        cur_set = [False] * n
        print_k_subsets_helper(cur_set, k, 0, 0)


def print_k_subsets_helper(cur_set, k, index, picked):
    """this recursive function gets a cur_set - list with n 'False', 'k' - the
    length of the subsets, index, and picked - the numbers of 'True's in the
    cur_set.
    When there are k 'True's in the cur_set, the function uses the 'print_list'
    function."""
    if k == picked:
        print_list(cur_set)
        return
    if index == len(cur_set):
        return
    cur_set[index] = True
    print_k_subsets_helper(cur_set, k, index + 1, picked + 1)

    cur_set[index] = False
    print_k_subsets_helper(cur_set, k, index + 1, picked)


def print_list(final_set):
    """This function gets the cur_list with k 'True's, and print the subset of
    all the indexes that contain 'True' in the cur_list."""
    comb = []
    for i in range(len(final_set)):
        if final_set[i]:
            comb.append(i)
    print(comb)


# Function number 2
def fill_k_subsets(n, k, lst):
    """This function gets two numbers - 'n' and 'k', and an empty list.
    The function will change the empty list to a list of all the k size subsets
    with the numbers from 0 to n-1, when every number in the subset, is bigger
    then the previous number"""
    if k <= n:
        cur_set = [False] * n
        fill_k_subsets_helper(cur_set, k, 0, 0, lst)


def fill_k_subsets_helper(cur_set, k, index, picked, lst):
    """this recursive function gets a cur_set - list with n 'False', 'k' - the
    length of the subsets, index, picked - the numbers of 'True's in the
    cur_set and a list of all the subsets until now (empty on the beginning).
    When there are k 'True's in the cur_set, the function uses the
    'update_list' function."""
    if k == picked:
        update_list(cur_set, lst)
        return
    if index == len(cur_set):
        return

    cur_set[index] = True
    fill_k_subsets_helper(cur_set, k, index + 1, picked + 1, lst)

    cur_set[index] = False
    fill_k_subsets_helper(cur_set, k, index + 1, picked, lst)


def update_list(final_set, lst):
    """This function gets the cur_list with k 'True's and the list of all the
    subsets until now, and add the subset of all the indexes that contain
    'True' in the cur_list, to the list."""
    comb = []
    for i in range(len(final_set)):
        if final_set[i]:
            comb.append(i)
    lst.append(comb)


# Function number 3
def return_k_subsets(n, k, index=0):
    """This recursive function gets tow numbers - 'n' and 'k', and a default
    index - 0. It returns a list of all the k size subsets with the numbers
    from 0 to n-1, when every number in the subset, is bigger then the previous
    number."""
    if index == k:
        if k == 0:
            return [[]]
        if k > n:
            return []
        else:
            new_list = []
            for i in range(n - k + 1):
                new_list.append([i])
            return new_list

    list_1 = return_k_subsets(n, k, index + 1)
    final_list = []
    for lst in list_1:
        if len(lst) < k:
            for i in range(lst[LAST] + 1, n):
                final_list.append(lst + [i])
        else:
            final_list.append(lst)
    return final_list
