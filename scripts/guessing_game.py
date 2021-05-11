import random

print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)
guessed_correctly = False

while not guessed_correctly:
    guess = int(input("Guess a number: "))

    if guess > number:
        print("Go lower")
    elif guess < number:
        print("Go higher")
    else:
        guessed_correctly = True

print("Correct!")