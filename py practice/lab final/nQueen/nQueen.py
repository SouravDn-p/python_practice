def isSafe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1
            if solveNQUtil(board, col + 1, N):
                return True
            board[i][col] = 0  # BACKTRACK

    return False

def printSolution(N):
    board = [[0] * N for _ in range(N)]

    if not solveNQUtil(board, 0, N):
        print("Solution does not exist")
        return False

    print(f"Solution found for {N} queens:")
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    return True

# Get user input
n = int(input("Number of queens to place:\n"))
printSolution(n)
