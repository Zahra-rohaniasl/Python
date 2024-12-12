import math  
import random  

class TicTacToe:  
    def __init__(self):  # Initialize the game board  
        self.board = self.make_board()  # Create a new game board  
        self.current_winner = None  # Track the current winner  

    def make_board(self):  
        return [' ' for _ in range(9)]  # Create a 3x3 board represented as a flat list  

    def print_board(self):  
        # Print the current state of the board  
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:  # Split the board into rows  
            print('| ' + ' | '.join(row) + ' |')  # Join each row with separators  

    def print_board_nums(self):  
        # Print a number board for user reference  
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]  
        for row in number_board:  
            print('| ' + ' | '.join(row) + ' |')  # Show numbers for each square  

    def make_move(self, square, letter):  # square: where the user wants to go (0-8), letter: 'X' or 'O'  
        if self.board[square] == ' ':  # Check if the square is empty  
            self.board[square] = letter  # Place the letter on the board  
            if self.winner(square, letter):  # Check for a winner  
                self.current_winner = letter  # Set the current winner  
            return True    
        return False  # Move was invalid  

    def winner(self, square, letter):  
        # Check for a winner  
        row_ind = math.floor(square / 3)  # Determine the row index  
        row = self.board[row_ind * 3:(row_ind + 1) * 3]  # Get the current row  
        if all([s == letter for s in row]):  # Check if all elements in the row match the letter  
            return True  
        
        col_ind = square % 3  # Determine the column index  
        column = [self.board[col_ind + i * 3] for i in range(3)]  # Get the current column  
        if all([s == letter for s in column]):  # Check if all elements in the column match the letter  
            return True  
        
        # Check diagonals if the square is in an even position  
        if square % 2 == 0:  
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Main diagonal  
            if all([s == letter for s in diagonal1]):  # Check if all elements match  
                return True  
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Anti-diagonal  
            if all([s == letter for s in diagonal2]):  # Check if all elements match  
                return True  
        
        return False  # No winner found  

    def empty_squares(self):  # Check if there are any empty squares  
        return ' ' in self.board  

    def num_empty_squares(self):   
        return self.board.count(' ')  # Count the number of empty squares  

    def available_moves(self):  
        return [i for i, x in enumerate(self.board) if x == ' ']  # List empty squares  

def play(game, x_player, o_player, print_game=True):  
    if print_game:  
        game.print_board_nums()  # Print the number board for reference  

    letter = 'X'  # Start with player X  
    while game.empty_squares():  # Continue until there are no empty squares  
        if game.num_empty_squares() == 1:  # If only one square is left, break the loop  
            square = game.available_moves()[0]  # Get the last available move  
        else:  
            if letter == 'X':  
                square = x_player.get_move(game)  # Get move from human player  
            else:  
                square = o_player.get_move(game)  # Get move from computer player  

        if game.make_move(square, letter):  # Make the move  
            if print_game:  
                print(letter + f' makes a move to square {square}')  
                game.print_board()  # Print the board after the move  
            if game.current_winner:  # Check if there's a winner  
                if print_game:  
                    print(letter + ' wins!')  # Announce the winner  
                return letter  # Return the winner  
            letter = 'O' if letter == 'X' else 'X'  # Switch players  

    if print_game:  
        print('It\'s a tie!')  # Announce a tie if the board is full without a winner  

class HumanPlayer:  
    def __init__(self, letter):  
        self.letter = letter  

    def get_move(self, game):  
        valid_square = False  
        val = None  
        while not valid_square:  
            square = input(self.letter + '\'s turn. Input move (0-8): ')  
            try:  
                val = int(square)  
                if val not in game.available_moves():  
                    raise ValueError  # Raise an error if the move is invalid  
                valid_square = True  # Valid move  
            except ValueError:  
                print('Invalid square. Try again.')  # Prompt for a valid input  
        return val  

class RandomComputerPlayer:  
    def __init__(self, letter):  
        self.letter = letter  

    def get_move(self, game):  
        square = random.choice(game.available_moves())  # Pick a random available move  
        print(self.letter + f' makes a move to square {square}')  # Announce the computer's move  
        return square  

if __name__ == '__main__':  
    x_player = HumanPlayer('X')  # Create a player for X  
    o_player = RandomComputerPlayer('O')  # Create a computer player for O  
    t = TicTacToe()  # Initialize the game  
    play(t, x_player, o_player)  # Start the game
