import random

def guessing_game():
    numbertoguess = random.randint(10, 50)
    attempt = 0
    guessed_correct = False
    print("Welcome to the guessing game!")
    print("Guess what number I chose between 10-50")
    while not guessed_correct:
        guess = int(input("What's your guess: "))
        attempt += 1
        if guess < numbertoguess:
            print("That's Low Try again")
        elif guess > numbertoguess:
            print("Too high Try again")
        else:
            print("Congratulations! You guessed it correctly")
            print(f"You had a total of {attempt} attempts")
            guessed_correct = True
guessing_game()