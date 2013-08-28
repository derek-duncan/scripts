#!/usr/bin/python
import os
from random import choice

guesses = []
wrongL = []
iLetter = ""
with open(os.path.join(os.path.dirname(__file__), 'words.txt')) as f:
    words = [line.rstrip('\n') for line in f.readlines()]
word = list(choice(words))
length = len(word)
blanks = ['_'] * length


def guessOpen():
    global guesses
    print(" ".join(blanks))

    def inputP():
        global iLetter
        iLetter = str(input('Enter your first letter: '))
        for let in iLetter:
            if let.isdigit():
                print("Not a letter!  Try again.")
                inputP()
        if len(iLetter) > 1:
            print('Your entry was too long.  Reenter your letter.')
            inputP()
    inputP()
    if iLetter not in guesses:
        guesses.append(iLetter)
    print("Guessed Letters: " + ", ".join(guesses))
    print(len(wrongL))
    if iLetter in word:
        rightL(iLetter)
    else:
        wrong(iLetter)


def rightL(l):
    global iLetter
    for mi, li in enumerate(word):
        if li == iLetter:
            blanks[mi] = iLetter
    if not checks():
        guessOpen()


def wrong(x):
    global wrongL
    wrongL.append(x)
    print ("\'" + x.upper() + "\'" + " was not found in the secret word!\n")
    print('\nYou have ' + str(len(wrongL)) +
          " missed guesses.  You have " + str(7 - (len(wrongL))) + " misses left!")
    if checks2():
        guessOpen()


def checks():
    global iLetter, wrongL, guesses, word, blanks, length
    if blanks == word:
        print("\n" + "".join(blanks) + "\n")
        print("Congrats! You won!  Play Again!")
        reset()
        guessOpen()
        return True
    else:
        return False


def checks2():
    if len(wrongL) == 7:
        print("Too many misses! The word was " +
              "".join(word) + ".  Try again!")
        reset()
        guessOpen()
        return False
    else:
        return True


def reset():
    global iLetter, wrongL, guesses, word, blanks, length
    word = list(choice(words))
    length = len(word)
    blanks = ['_'] * length
    guesses = []
    wrongL = []
    iLetter = ""


try:
    print("Word has been chosen.  Make your first guess wisely!  You only have 7 misses\n", guessOpen())
except KeyboardInterrupt:
    print('\nThanks for Playing!')
