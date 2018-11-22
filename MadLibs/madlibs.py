# CS 1.1
# Project: Mad Libs
# Written By: Asim Zaidi

# List of Requirements
# Write madlibs program
#list or string, or some different data structure of stories to change, choose from set of stories.
# ask for 5 user inputs line by line.
# randomize user inputs
# insert mad libs into template and return that to user.
# error check test inputs, what happens if user inputs whitespace only.

# import statements
#Ikey's sick color idea
import colors as c
from time import sleep
import sys
import random

def exiting():
    print_slowly("Wow really, okay.. you'll be back though.")
    exit()

def print_slowly(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.05)
    print('')

# User Questionare Function
def userQuestionare(selectedStory):
    adjective1 = input("Tell me an adjective, and click enter. ")
    adjective2 = input("Tell me an another adjective, and click enter. ")
    noun1 = input("Tell me a noun (plural), and click enter. ")
    noun2 = input("Tell me another noun, and click enter. ")

    if noun2 == "exit" or noun1 == "exit" or adjective2 == "exit" or adjective1 == "exit":
        exiting()

    # randomize inputs
    nounList = [noun1,noun2]
    adjList = [adjective1, adjective2]
    random.shuffle(nounList)
    random.shuffle(adjList)

    if selectedStory=="funny":
        print("I have been having the " + adjList[0] + " dreams. I dreampt last night that i looked exactly like the girl from wendys restaurants. I even had a " + adjList[1] + " full of those checkered dresses and nothing else. Some of my other " + nounList[0] + " dreams that I had lately were I was a genie in a " + nounList[1] + " but no one would let me out.")
    if selectedStory=="childrens":
        print("Today a superhero named captain rainbow came to our school to talk to us about their job. She said the most important skill you need to know to do her job is to be able to laugh around (a) " + adjList[0] + " " + nounList[0] + ". She said it was easy for her to learn her " + nounList[1] + " because she loved how her thoughts were so " + adjList[1] + "!")
    if selectedStory=="adult":
        print(nounList[0] + " be " + adjList[0] + " like they be " + adjList[1] + " when they're chilling and playing poker with their " + nounList[1] + ".")

# start the story printing
print_slowly(c.green + "Welcome to Mad Libs. Created by " + c.yellow + "Asim Zaidi." + c.end)
print_slowly("Would you like a funny, childrens, or adult MadLib to play with?")
print_slowly("At any time enter 'exit' to quit the cool game.")
# collect the selected story from the user input, by validating the input (if it's A, B, or C. Otherwise, print error and try again)
userStory = ""
isRunning = True
while isRunning==True:
    userChoice = input("Enter " + c.blue + "A" + c.end + " for funny\nEnter " +c.blue + "B" + c.end + " for childrens\nEnter " + c.blue + "C" + c.end +  " for adults\n")
    if userChoice == "exit":
        exiting()
    if userChoice == "A" or userChoice=="a":
        userStory="childrens"
        isRunning = False
    elif userChoice == "B" or userChoice=="b":
        userStory="funny"
        isRunning = False
    elif userChoice == "C" or userChoice=="c":
        userStory="adult"
        isRunning = False
    else:
        print_slowly("Please type in A, B or C. Other inputs are not accepted at this time.")

# after selecting the story from the user, start the questionare
print_slowly(c.magenta+"Okay let's begin.. answer these questions ;)" + c.end)
userQuestionare(userStory)
