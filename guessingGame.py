import random

num = str(random.randint(1, 100))
print("It's about time to play a guessing game!")

countA = 1
guessed = 0


def askQ():
    global guessed
    initNum = input("Enter your first guess: ")
    if initNum < num:
        print("\nGuess is too low!\n")
        guessed = 0
    elif initNum > num:
        print("\nGuess is too high!\n")
        guessed = 0
    elif initNum == num:
        print("\nCorrect! It took you " + str(countA) + " times to guess the number!")
        guessed = 1
while guessed == 0:
    askQ()
    countA += 1

print("Great Job!")
