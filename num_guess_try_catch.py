#!/usr/bin/env python3
# Created By: Titwech Wal
# Date: April.5. 2022

# program asks the user for an integer
# then tells them if they're right

from colorama import Fore
import random


def main():
    # a number between 1 and 100
    random_variable = random.randint(1, 10)

    # try catch
    try:
        # string into integer
        user_guess = input("Enter a integer between (0-10): ")
        user_guess_as_int = int(user_guess)

        # check if number is correct or incorrect
        if user_guess == random_variable:
            print(Fore.GREEN + "You guessed right")

        else:
            print(Fore.RED + "You guessed wrong the integer is: {}"
                  .format(random_variable))
            print("")

    except Exception:
        print("That is not a integer")
        print("")

    finally:
        print(Fore.YELLOW + "Thanks for playing!")


if __name__ == "__main__":
    main()
