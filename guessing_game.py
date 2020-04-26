"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
Mike Conner 
04/25/2020
--------------------------------
"""

import random


#  Start the game!!! :)
def start_game():
    
    print("\nWelcome to the Guessing Game!\n")
    
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
        
    random_number  = random.randint(lowest_number, highest_number)
    high_score = highest_number    
    print("\nThis is the first game so the High score will be set to {}.\n".format((highest_number - lowest_number) + 1))
    
    while True:
        try:
            users_guess = int(input("Please enter a number between {} and {}...  ".format(lowest_number, highest_number)))
            if (users_guess < lowest_number) or (users_guess > highest_number):
                raise ValueError
        except ValueError:
            print("\nYour guess must be a number in the range {}...{}. Please try again.\n".format(lowest_number, highest_number))
        else:
            number_of_attempts = 1
            break
    
    while True:
        
        if random_number == users_guess:
            print("\nThat's correct!\nThat took you {} attempt(s).\n".format(number_of_attempts))
            if number_of_attempts < high_score:
                print("CONGRATS!!! You have the new high score!\n")
                high_score = number_of_attempts
            else:
                print("The current High Score is {} attempt(s).\nBetter luck next time...".format(high_score))
                
            play_again = input("Do you want to play again? (y/n). ")
            
            if play_again.lower() == 'n':
                print("\n\nIt's been a lot of fun! Come back and play again soon! :D\n\n")
                break
            else:
                print("\nGood luck, the current High Score is {}.\n".format(high_score))
                random_number = random.randint(lowest_number, highest_number)
                number_of_attempts = 0
                while True:
                    try:
                        users_guess = int(input("Please enter a number between {} and {}...  ".format(lowest_number, highest_number)))
                        if (users_guess < lowest_number) or (users_guess > highest_number):
                            raise ValueError
                    except ValueError:
                        print("Your guess must be a number in the range {}...{}. Please try again.\n".format(lowest_number, highest_number))
                    else:
                        number_of_attempts += 1
                        break
        else:
            if random_number > users_guess:
                print("\nSorry, that is not correct. The number is higher.")
            else:
                print("\nSorry, that is not correct. The number is lower.")
                
            while True:
                try:
                    users_guess = int(input("\nPlease enter a number between {} and {}...  ".format(lowest_number, highest_number)))
                    if (users_guess < lowest_number) or (users_guess > highest_number):
                        raise ValueError
                except ValueError:
                    print("\nYour guess must be a number in the range {}...{}. Please try again.".format(lowest_number, highest_number))
                else:
                    number_of_attempts += 1
                    break

                    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
