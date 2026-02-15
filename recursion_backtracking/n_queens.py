def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve(board, row, n):
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve(board, row + 1, n)


n = int(input("Enter number of queens: "))
board = [-1] * n
solve(board, 0, n)
