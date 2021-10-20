# Imports choice method random module
from random import choice

# Defines a random magic number
magicNum = choice(range(1,10))

def guess():
    try:
        guessed = int(input("Enter guess (1-9): "))
    except ValueError as e:
        guess()
    else:
        return guessed

guessed_ = 0

while(guess != magicNum):
    guessed_ = guess()
    if guessed_ == magicNum:
        print("Well guessed!")
        break



