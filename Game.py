import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

while True:
    # Get the user's guess
    user_guess = int(input("Enter your guess (1-100): "))

    # Check if the guess is correct
    if user_guess == secret_number:
        print("You guessed it right!!")
        break

    # Provide feedback based on the guess
    elif user_guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")