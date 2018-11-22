Spaceman Project
Description
Spaceman is a guessing game. There is a mystery word which the user tries to guess one letter at a time.

Requirements
If the guessed letter is in the mystery word, the position(s) of the letter(s) are revealed in the placeholders.
If a guessed letter occurs more than once in the word all the places that letter occurs are revealed.
If a player guesses all the letters in the word, they win the game.
For each incorrect guess a part of the Spaceman (a 7 part drawing of a Spaceman) is drawn.
If all 7 parts of the Spaceman are drawn then the player loses the game.

# Spaceman Pseudocode

Hangman Brainstorm/Rules:
There will be a random word that is a mystery to the user.
User is displayed the amount of letters in the word with underscores.
The program prompt's the user to guess a letter in the word
We store the letters the user guesses in a list of guessed words.
If the guessed letter is within the secret word, we display that character(s)
If the letter is incorrect, we add a part to the hangman ACSII code.
the Hangman has 7 parts before it explodes and the user loses.


Spaceman program pseudocode
**************************
Create class Hangman
Create a function to generate a secret word.
Create function to get user input for guesses.
Sep function to check char or string
display function
Store guesses into a list and check if it is in the secret word or not.
Create a hangman ascii code function.
