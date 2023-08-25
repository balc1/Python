from art import logo
import random

print(logo)
y = random.randint(1, 100)

print(
    f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPssst, the correct answer is {y}"
)

zorluk = input("Choose a difficulty. Type 'easy' or 'hard':")
hak = 0

if zorluk == "easy":
    hak = 10
elif zorluk == "hard":
    hak = 5

while hak > 0:
    print(f"You have {hak} attempts remaining to guess the number.")
    guess = input("Make a guess:")
    if int(guess) > y:
        print("Too high.\nGuess again.")
    elif int(guess) < y:
        print("Too low.\nGuess again.")
    elif int(guess) == y:
        print(f"You got it! The answer was {guess}.")
        hak -= 10
    hak -= 1
