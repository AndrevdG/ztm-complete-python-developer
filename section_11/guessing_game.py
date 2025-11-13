# Write a program that lets the player provide two arguments
# at startup and they then have to guess a random number between those
# arguments.
# Keep asking till the user guesses it right

# f.i. to guess a number between 1 and 20
# python3 guessing_game.py 1 20
from sys import argv
from random import randint


if __name__ == "__main__":
    if len(argv) == 3:
        try:
            low = int(argv[1])
            high = int(argv[2])
        except TypeError:
            print('please provide only 2 integer numbers to the program')
            exit(1)
        secret_number = randint(low, high)

        while True:
            try:
                user_choice = int(input(f'Please pick a number between {low} and {high}: '))
            except TypeError:
                print('only provide an integer number please')
            except KeyboardInterrupt:
                print(f'\nyou did not guess it!, the number was {secret_number}')
                exit(0)
            if user_choice == secret_number:
                break

        print(f'You guessed it! {secret_number} was the correct answer')
    else:
        print('please provide 2 (int) numbers as argument for our guessing game')
