#N-Queen problem

=>Function solve():
    1. Initialize a board of size N x N with all values set to 0.
    2. Call solve_n_queens(board, 0) to start solving the problem from row 0.
    3. If solve_n_queens(board, 0) returns True:
        - Print "Solution found" and display the board.
    4. Else, print "No solution exists."

=>Function solve_n_queens(board, row):
    1. If row >= N:
        - All queens are placed successfully, so print the board configuration.
        - Return True.
    2. For each column col in the current row (col = 0 to N-1):
        1. Check if placing a queen at (row, col) is safe using is_safe(board, row, col).
        2. If safe:
            1. Place the queen at (row, col) by setting board[row][col] = 1.
            2. Call solve_n_queens(board, row + 1) to place the next queen.
            3.. If solve_n_queens(board, row + 1) returns True:
                - Return True (solution found).
            4. If not, backtrack by setting board[row][col] = 0 and try the next column.
    3. Return False if no solution is found for the current row.
    
=>Function is_safe(board, row, col):
    1. For each row i from 0 to row - 1:
        1, Check if board[i][col] == 1 (same column).
            - If true, return False (column is not safe).
    2. For each upper-left diagonal (i, j) where i decreases and j decreases:
        1, Check if board[i][j] == 1 (same diagonal).
            - If true, return False (diagonal is not safe).
    3. For each upper-right diagonal (i, j) where i decreases and j increases:
        1, Check if board[i][j] == 1 (same diagonal).
            - If true, return False (diagonal is not safe).
    4. Return True if no conflicts were found.
