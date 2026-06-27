# Number guessing game program by @Skavam on GitHub

import random 

def main():
    attempts = 0
    number_to_guess = generate_random_number()
    
    while True:

        player_choice = int(input("Guess a number between 1 and 100: "))

        if player_choice == number_to_guess:
            print(f"Congratulations! You guessed the correct number. It was {number_to_guess}.")
            break

        elif player_choice < number_to_guess:
            print("Too low! Try again.")
            attempts += 1

        elif player_choice > number_to_guess:
            print("Too high! Try again.")
            attempts += 1

        else:
            print("Invalid input. Please enter a number between 1 and 100.")

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    main()
