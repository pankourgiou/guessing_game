import random

# Set the range for the random number
lower_limit = 1
upper_limit = 100

# Generate a random number
target_number = random.randint(lower_limit, upper_limit)

print(f"Welcome to the Guessing Game! Guess the number between {lower_limit} and {upper_limit}.")

# Initialize the guess count and user guess
guess_count = 0
user_guess = None

# Start the while loop for guessing
while user_guess != target_number:
    # Get user input and increment guess count
    user_guess = int(input("Enter your guess: "))
    guess_count += 1
    
    # Check if the guess is correct
    if user_guess < target_number:
        print("Too low! Try again.")
    elif user_guess > target_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {guess_count} tries.")

# End of the game
print("Thanks for playing!")
