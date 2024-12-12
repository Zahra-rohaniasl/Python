import random  
import re  

# Create a board object for the game  
class Board:  
    def __init__(self, dim_size, num_bombs):  
        self.dim_size = dim_size  # Size of the board (dim_size x dim_size)  
        self.num_bombs = num_bombs  # Number of bombs to place on the board  
        self.board = self.make_new_board()  # Plant the bombs on the board  
        self.assign_values_to_board()  # Assign numbers to indicate neighboring bombs  
        self.dug = set()  # Set to track dug locations  

    def make_new_board(self):  
        # Generate a new board and plant bombs  
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]  
        
        bombs_planted = 0  
        while bombs_planted < self.num_bombs:  
            loc = random.randint(0, self.dim_size**2 - 1)  # Random location for bomb  
            row = loc // self.dim_size  # Determine row index  
            col = loc % self.dim_size  # Determine column index  

            if board[row][col] == '*':  # Skip if bomb is already planted  
                continue  
            
            board[row][col] = '*'  # Plant the bomb  
            bombs_planted += 1  

        return board  

    def assign_values_to_board(self):  
        # Assign values to each cell indicating the number of neighboring bombs  
        for r in range(self.dim_size):  
            for c in range(self.dim_size):  
                if self.board[r][c] == '*':  # Skip bomb locations  
                    continue  
                self.board[r][c] = self.get_num_neighbor_bombs(r, c)  # Count neighboring bombs  

    def get_num_neighbor_bombs(self, row, col):  
        # Count bombs in neighboring cells  
        num_neighbor_bombs = 0  
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):  
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):  
                if r == row and c == col:  # Skip the current cell  
                    continue  
                if self.board[r][c] == '*':  # Check if there's a bomb  
                    num_neighbor_bombs += 1  

        return num_neighbor_bombs  # Return total number of neighboring bombs  

    def dig(self, row, col):  
        # Dig at the specified location and return True if safe, False if bomb  
        self.dug.add((row, col))  # Track the dug location  

        if self.board[row][col] == '*':  
            return False  # Hit a bomb  
        elif self.board[row][col] > 0:  
            return True  # Dug a safe spot with neighboring bombs  
        
        # Recursively dig neighboring cells  
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):  
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):  
                if (r, c) in self.dug:  # Skip already dug locations  
                    continue  
                self.dig(r, c)  # Recursive dig  

        return True  # Return True if no bomb was hit directly  

    def __str__(self):  
        # Return a string representation of the board for display  
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]  
        for row in range(self.dim_size):  
            for col in range(self.dim_size):  
                if (row, col) in self.dug:  # Display dug cells  
                    visible_board[row][col] = str(self.board[row][col])  
                else:  
                    visible_board[row][col] = ' '  # Show blank for undug cells  

        # Combine visible cells into a string  
        string_rep = ''  
        for row in visible_board:  
            string_rep += ' | '.join(str(cell) for cell in row) + '\n'  
        return string_rep  

# Function to play the game  
def play(dim_size=10, num_bombs=10):  
    # Step 1: Create the board and plant the bombs  
    board = Board(dim_size, num_bombs)  # Initialize the board  
    
    # Step 2: Show the user the board and prompt for digging input  
    while len(board.dug) < board.dim_size**2 - num_bombs:  
        print(board)  # Display the current state of the board  
        user_input = re.split(',(\\s)*', input('Where do you want to dig? Input as row, col: '))  
        
        # Parse user input and validate coordinates  
        row, col = int(user_input[0]), int(user_input[-1])  
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:  
            print('Invalid location, try again.')  
            continue  

        # If the location is valid, dig there  
        safe = board.dig(row, col)  
        if not safe:  
            # Dug a bomb  
            break  # Game over  

    # Check the outcome of the game  
    if safe:  
        print('Congratulations! You are the winner!!!')  
    else:  
        print('Game over!')  

        # Reveal the whole board  
        board.dug = {(r, c) for r in range(board.dim_size) for c in range(board.dim_size)}  
        print(board)  

if __name__ == '__main__':  # Entry point for the program  
    play()
