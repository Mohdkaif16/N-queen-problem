def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()
def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True
def solve_n_queens(board, row, N):
    if row >= N:
        print_solution(board, N)
        return True

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  
            if solve_n_queens(board, row + 1, N):
                return True
            board[row][col] = 0 
    return False
def solve(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_n_queens(board, 0, N):
        print("No solution exists.")
    else:
        print("Solution found!")

# Main execution starts here
n = int(input("Enter the number of queens: "))
if n <= 0 or n % 2 != 0:
    print("Enter an even number of queens greater than 0.")
else:
    solve(n)
