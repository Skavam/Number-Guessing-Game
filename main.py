# Number guessing game program by @Skavam on GitHub

import random 
from colorama import Fore

def main():
    attempts = 0
    number_to_guess = generate_random_number()
    
    while True:

        player_choice = int(input(Fore.WHITE +"Guess a number between 1 and 100: "))

        if player_choice == number_to_guess:
            print(Fore.GREEN + f"Congratulations! You guessed the correct number. It was {number_to_guess}.")
            print(Fore.YELLOW + f"You guessed it in {attempts} attempts.")
            print(Fore.WHITE + "Thanks for playing!")
            break

        elif player_choice < 1 or player_choice > 100:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 100.")

        elif player_choice < number_to_guess:
            print(Fore.LIGHTBLUE_EX + "Too low! Try again.")
            attempts += 1

        elif player_choice > number_to_guess:
            print(Fore.LIGHTBLUE_EX + "Too high! Try again.")
            attempts += 1

        else:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 100.")

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    main()
