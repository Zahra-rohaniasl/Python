# Finds the next empty row and column in the puzzle; empty cells are represented with -1.  
# Returns a tuple (row, column) if an empty cell is found, or (None, None) if the puzzle is full.  
def find_next_empty(puzzle):  
    for r in range(9):  
        for c in range(9):  # Iterate through each cell in the 9x9 grid  
            if puzzle[r][c] == -1:  # If the cell is empty  
                return r, c  # Return the coordinates of the empty cell  
    return None, None  # Return None if no empty cells are found  

# Checks if placing a guess at the specified row and column of the puzzle is valid.  
# Returns True if valid, False otherwise.  
def is_valid(puzzle, guess, row, col):  
    # Check the row for the same guess  
    row_vals = puzzle[row]  
    if guess in row_vals:  # If the guess already exists in the row  
        return False  # Not a valid guess  
    
    # Check the column for the same guess  
    col_vals = [puzzle[i][col] for i in range(9)]  # Create a list of values in the column  
    if guess in col_vals:  # If the guess already exists in the column  
        return False  # Not a valid guess  
    
    # Check the 3x3 square for the same guess  
    row_start = (row // 3) * 3  # Determine the starting row for the 3x3 box  
    col_start = (col // 3) * 3  # Determine the starting column for the 3x3 box  
    
    # Examine each cell in the 3x3 box  
    for r in range(row_start, row_start + 3):  
        for c in range(col_start, col_start + 3):  
            if puzzle[r][c] == guess:  # If the guess exists in the box  
                return False  # Not a valid guess  

    # If all checks pass, the guess is valid  
    return True  

# Solves the Sudoku puzzle using a backtracking algorithm.  
# The function modifies the puzzle in place if a solution is found.  
# Returns True if a solution exists, False otherwise.  
def solve_sudoku(puzzle):  
    row, col = find_next_empty(puzzle)  # Find the next empty cell  
    
    # If there are no empty cells left, the puzzle is solved  
    if row is None:  
        return True  
    
    # Try each guess from 1 to 9  
    for guess in range(1, 10):  
        if is_valid(puzzle, guess, row, col):  # Check if the guess is valid  
            puzzle[row][col] = guess  # Place the valid guess in the puzzle  
            
            # Recursively attempt to solve the puzzle with the current guess  
            if solve_sudoku(puzzle):  
                return True  # If the puzzle is solved with this guess, return True  
    
    # If the guess does not lead to a solution, reset the cell and try next guess  
    puzzle[row][col] = -1  # Reset the cell to empty  
    
    # If no valid guesses lead to a solution, return False  
    return False  

# Example Sudoku for testing  
if __name__ == '__main__':  
    example_board = [  # Define a 9x9 Sudoku board with -1 indicating empty cells  
        [4, -1, -1,   -1, -1, 2,   8, 3, -1],  
        [-1, 8, -1,   1, -1, 4,   -1, -1, 2],  
        [7, -1, 6,   -1, 8, -1,   5, -1, -1],

        [1, -1, -1,   -1, -1, 7,   -1, 5, -1],  
        [2, 7, -1,   5, -1, -1,   -1, 1, 9],  
        [-1, 3, -1,   9, 4, -1,   -1, -1, 6],

        [-1, -1, 8,   -1, 9, -1,   7, -1, 5],  
        [3, -1, -1,   8, -1, 6, -1, 9, -1],  
        [-1, 4, 2,   7, -1, -1,   -1, -1, 3]  
    ]  

    if solve_sudoku(example_board):  
        print("Sudoku solved!")  # Print success message if the puzzle is solved  
    else:  
        print("No solution exists.")  # Print failure message if unsolvable  
    print(example_board)  # Display the solved board or the tried values
