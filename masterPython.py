#Number guessing game

import random

def play_number_guessing_game():

    #take a random number
    secret_num = random.randint(1, 100)
    guesses_left = 7

    print("Welcome to the Guessing Number Game! ")
    print("I am guessing a number between 1 and 100 ")

    while guesses_left > 0:
        guess = int(input(f"You have {guesses_left} guesses left. What's your guess? "))
        
        if guesses_left == 7 :
            print("You have 7 chance to guess. Good luck! ")
        elif guess < secret_num :
            print("Too low! Try again. ")
        elif guess > secret_num :
            print("Too high! Try again. ")
        elif guess == secret_num :
            print("Congratulations! You guessed the number! ")
            return
        
        guesses_left -= 1

    print(f"Sorry, you've run out of guesses, the right answer is {secret_num}")

play_number_guessing_game()

