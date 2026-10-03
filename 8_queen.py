def is_safe(board, row, col):
    for i in range(row):
        # Same column
        if board[i] == col:
            return False

        # Same diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_8_queens(board, row):
    if row == 8:
        print_board(board)
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col

            if solve_8_queens(board, row + 1):
                return True

            board[row] = -1

    return False


def print_board(board):
    for row in range(8):
        for col in range(8):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


board = [-1] * 8

if solve_8_queens(board, 0):
    print("8-Queen solution found!")
else:
    print("No solution exists.")
