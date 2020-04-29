"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
Mike Conner
04/25/2020
--------------------------------
"""

import random


def print_welcome_message():
    print("""
-----------------------------
Welcome to the Guessing Game!
-----------------------------\n""")

def set_range():
    while True:
        try:
            lowest_number  = int(input("Enter the lowest number you want to guess.  "))
        except ValueError:
            print("\nYou must enter a number. Please try again.\n")
        else:
            break

    while True:
        try:
            highest_number = int(input("\nEnter the highest number you want to guess.  "))
        except ValueError:
            print("\nYou must enter a number. Please try again.")
        else:
            break


    while highest_number <= lowest_number:
        print("\nSorry, the highest number must be higher than the lowest number.\n")
        while True:
            try:
                highest_number = int(input("Enter the highest number you want to guess.  "))
            except ValueError:
                print("You must enter a number. Please try again.")
            else:
                break

    return lowest_number, highest_number


def set_initial_high_score(lowest_number, highest_number):
    high_score = highest_number
    print("\nThis is the first game so the High score will be set to {}.\n".format(
        (highest_number - lowest_number) + 1)
    )

    return high_score

def get_users_guess(lowest_number, highest_number, number_of_attempts):
    while True:
        try:
            users_guess = int(input("Please enter a number between {} and {}...  ".format(
            lowest_number, highest_number))
        )
            if (users_guess < lowest_number) or (users_guess > highest_number):
                raise ValueError
        except ValueError:
            print("\nYour guess must be a number in the range {}...{}. Please try again.\n".format(
            lowest_number, highest_number)
        )
        else:
            if number_of_attempts == 0:
                number_of_attempts = 1
            else:
                number_of_attempts += 1
            break

    return users_guess, number_of_attempts


def correct_answer(number_of_attempts, high_score):
    print("\nThat's correct!\nThat took you {} attempt(s).\n".format(number_of_attempts))
    if number_of_attempts < high_score:
        print("CONGRATS!!! You have the new high score!\n")
        high_score = number_of_attempts
    else:
        print("""
The current High Score is {} attempt(s).
Better luck next time...\n""".format(high_score)
)

    return high_score

def start_game():
    print_welcome_message()

    lowest_number, highest_number = set_range()

    random_number  = random.randint(lowest_number, highest_number)

    number_of_attempts = 0

    high_score = set_initial_high_score(lowest_number, highest_number)

    users_guess, number_of_attempts = get_users_guess(
        lowest_number, highest_number, number_of_attempts
    )

    while True:
        if random_number == users_guess:
            high_score = correct_answer(number_of_attempts, high_score)

            play_again = input("Do you want to play again? (y/n). ")

            if play_again.lower() == 'n':
                print("""
\n------------------------------------------------------
It's been a lot of fun! Come back and play again soon!
------------------------------------------------------\n\n"""
)
                break
            else:
                print("\nGood luck, the current High Score is {}.\n".format(high_score))
                random_number = random.randint(lowest_number, highest_number)
                number_of_attempts = 0
                users_guess, number_of_attempts = get_users_guess(
                    lowest_number, highest_number, number_of_attempts
                )
        else:
            if random_number > users_guess:
                print("\nSorry, that is not correct. The number is higher\n.")
            else:
                print("\nSorry, that is not correct. The number is lower.\n")

            users_guess, number_of_attempts = get_users_guess(
                lowest_number, highest_number, number_of_attempts
            )


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
