import random

def play_game():
    print("Welcome to Guess the Number!")
    
    # Set the range for the number to guess
    low = 1
    high = 100
    number_to_guess = random.randint(low, high)
    
    attempts = 0
    guessed = False
    
    print(f"Guess the number between {low} and {high}.")

    # Start the guessing loop
    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is too low, too high, or correct
            if guess < low or guess > high:
                print(f"Please guess a number between {low} and {high}.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    play_game()
