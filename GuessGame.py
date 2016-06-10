import random


def the_guess_Game():
    number = random.randrange(1, 10)
    guess = int(input("Guess a number between 1 and 100 \n"))
    numberOfShoots = 0;

    while guess != number:
        if guess > number:
            numberOfShoots += 1
            print("Your guess number is too big")
        elif guess < number:
            numberOfShoots += 1
            print("Your guess number too small")
        guess = int(input("Try again dont give up \n"))

    print("\n\nGreat job your got the number in ", numberOfShoots, "guesses!")


the_guess_Game()
