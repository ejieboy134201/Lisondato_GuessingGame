import random

# Generate a random number between 1 and 10
hidden_number = random.randint(1, 10)

# Number of chances
chances = 3

# Game loop
for attempt in range(chances):
    # Get user's guess
    guess = int(input(f"Guess the number (between 1 and 10): "))
    
    # Check if the guess is correct
    if guess == hidden_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        if guess < hidden_number:
            print("Try again! The hidden number is higher.")
        else:
            print("Try again! The hidden number is lower.")
else:
    print(f"Sorry, you ran out of chances. The hidden number was {hidden_number}.")
