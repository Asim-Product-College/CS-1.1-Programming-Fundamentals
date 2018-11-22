import random
import sys
# import os
class Hangman:

    def __init__(self):
        pass
    wrong=0
    running=True
    listOfGuesses = []
    lenOfGuess = 0
    # this func returns a secret word from a pre set list of words using the built in random function in Python
    def generateRandomSecretWord(self):
        words = ("sonder", "vicinity")
        secretWord = random.choice(words)
        return secretWord

    # this func converts our secret word into a secret list that will slowly unveil in a later func.
    def secretWordToSecretList(self):
        secretWordListDisplay=[]
        for i in secretWord:
            secretWordListDisplay.append("_")
        return secretWordListDisplay

    # this fun was made to simply display the secret lists' current condition.
    def displaySecretWordListDisplay(self):
        print(secretWordListDisplay)

    # this func holds the wrong guesses and hangman ascii art in a string list.
    def displayHangman(self):
        # hangman ascii list starting from 0, 7 tries till he dies.
        self.hangman = (
            """
               _________
                |/
                |
                |
                |
                |
                |
                |___
                """,
            """
               _________
                |/   |
                |
                |
                |
                |
                |
                |___
                H""",
            """
               _________
                |/   |
                |   (_)
                |
                |
                |
                |
                |___
                HA""",
            """
               ________
                |/   |
                |   (_)
                |    |
                |    |
                |
                |
                |___
                HAN""",
            """
               _________
                |/   |
                |   (_)
                |   -|
                |    |
                |
                |
                |___
                HANG""",
            """
               _________
                |/   |
                |   (_)
                |   -|-
                |    |
                |
                |
                |___
                HANGM""",
            """
               ________
                |/   |
                |   (_)
                |   /|-
                |    |
                |   /
                |
                |___
                HANGMA""",
            """
               ________
                |/   |
                |   (_)
                |   /|-
                |    |
                |   - -
                |
                |___
                HANGMAN"""
        )
        print(self.hangman[self.wrong])

    def startGame(self):
        print("Welcome to Hangman...")

    # def displayWordArt():

    def getUserGuess(self):
        userGuess=""
        invalid=True
        stillIncorrectInput = True
        # while invalid:
        #     # try:
        #     #     userGuess = input("\nChoose a letter: ")
        #     # except EOFError:
        #     #     print("Alright zuck.. let's play by the rules..")
        #     # finally:
        userGuess = input("\nChoose a letter: ")
        userGuess = userGuess.lower()
        # logic to check if user input is valid, if not, keep prompting them to reenter or if they already entered in the char.

        if len(userGuess) != 1 or userGuess in self.listOfGuesses or userGuess.isalpha() != True:
            while stillIncorrectInput:
                userGuess = input("\nPlease choose only 1 leter character/a char you haven't chosen Choose again: ")
                if len(userGuess) == 1 and userGuess not in self.listOfGuesses and userGuess.isalpha() == True:
                    stillIncorrectInput = False
                # invalid=False
        return userGuess

    def storeUserGuess(self):
        # this didn't work at first because userGuess would save into this listOfGuesses..
        # so this if statement would trigger every time, even for new letters.
        # So we just have to move it before we store the guess into the list!
        #logic to check if user guess has already appeared, then just tell them to guess again!
        # userGuess=""
        # while userGuess in self.listOfGuesses:
        #     print("You've already chosen this letter before.. choose something new!")
        #     userGuess = self.getUserGuess()
        self.listOfGuesses.append(userGuess)
        print("Your guesses so far: " + str(self.listOfGuesses))

    def checkUserGuess(self, userGuess, secretWordListDisplay, secretWord):
        found = False
        indexTrack = 0

        for i in secretWord:
            if userGuess == i:
                secretWordListDisplay[indexTrack] = i
                found = True
            indexTrack+=1
            # if that guess is not found in our string, iterate the wrong var
            # to show the next part of hangman when it's ran.
        if found == False:
            print("Wrong Guess :(")
            self.wrong+=1
            # check for game over
            if self.wrong == 7:
                print(self.hangman[self.wrong])
                print("Game Over!")
                print("The word was... " + secretWord)
                sys.exit()
        if "_" not in secretWordListDisplay:
            # secretWordListDisplay[indexTrack] = userGuess
            print(secretWordListDisplay)
            print("you winnnn!")
            sys.exit()
        # call this func to display the word display updated.
        # self.displaySecretWordListDisplay()

# Call Functions
hangman = Hangman()

secretWord = hangman.generateRandomSecretWord()
hangman.startGame()
secretWordListDisplay = hangman.secretWordToSecretList()
while hangman.running == True:
    # display the line for the word
    displaySecretWordLine = hangman.displaySecretWordListDisplay()
    # display hangman
    result = hangman.displayHangman()
    # get User guess
    userGuess = hangman.getUserGuess()
    # store user guess
    listOfGuesses = hangman.storeUserGuess()
    # check user guess
    hangman.checkUserGuess(userGuess, secretWordListDisplay, secretWord)

    # for some reason this isn't working.
    print("\033c")

# peer code review notes
    # add logic to make caps/lower caps the same.
    # make your comments show WHY behind your code.
    # less cognitive overload to see things nearby than over a stretch, so just name var's when you need them in
    # python (script language). Java is different.
    # Create a whole ass error handling function and call it throughout the code..?
    # avoid the ripple of changes, tight cuppling.. global vars is a way to avoid it, but not a good thing usually..
    # or sometimes put things into a list can help.
    # code smell: passing a ton of parameters..
