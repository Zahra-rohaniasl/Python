import random  

# Function to allow the user to guess a randomly generated number  
def guess(x):  
    random_number = random.randint(1, x)  # Generate a random number between 1 and x  
    guess = 0  # Initialize user's guess  
    while guess != random_number:  # Continue until the guess matches the random number  
        guess = int(input(f'Guess a number between 1 and {x}: '))  # Prompt user for a guess  
        if guess < random_number:  # If guess is too low  
            print('Sorry, try again! Too low!')  
        elif guess > random_number:  # If guess is too high  
            print('Sorry, try again! Too high!')  
    print('Yay, congrats! You have guessed the correct number!')  

# Function for the computer to guess the user's number  
def computer_guess(x):  
    low = 1  # Set the lowest possible number  
    high = x  # Set the highest possible number  
    feedback = ''  # Initialize feedback from the user  
    while feedback != 'c':  # Loop until the computer guesses correctly  
        if low != high:  
            guess = random.randint(low, high)  # Generate a guess within the current range  
        else:  
            guess = low  # If low equals high, this is the only possible guess  
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()  # Get user feedback  
        if feedback == 'h':  # If the guess is too high  
            high = guess - 1  # Adjust the range  
        elif feedback == 'l':  # If the guess is too low  
            low = guess + 1  # Adjust the range  
    print(f'Yay! The computer finally guessed the number, {guess}, correctly!')  

# Start the computer guessing game  
computer_guess(10)
