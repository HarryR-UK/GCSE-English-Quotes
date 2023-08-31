from hashlib import new
import os
import time
import random


quoteFile = open("CCQuotes.txt", "r")
noQuotes = len(quoteFile.readlines())
points = 0

def showQuote():
    newQuote = ""
    print("revealed quote to remember")
    randQuote = random.randint(1,noQuotes)
    quoteFile = open("CCQuotes.txt", "r")
    for line in quoteFile:
        quotes = line.split(";")
        if randQuote == int(quotes[0]):
            newQuote = str(quotes[1])
    time.sleep(1)
    print(newQuote)
    time.sleep(1)
    gone_ = input("type anything to get rid of the quote: \n")
    if gone_ != None:
        os.system("clear")
    


guess = True
while guess == True:
    quoteFile = open("CCQuotes.txt", "r")
    gotRight = False
    randNum = random.randint(1,3)
    if randNum == 1:
        showQuote()
    uinput = input("Please enter a quotation from the quotes selection, or type 'EXIT' to end the game: \n\n\t").upper()
    if uinput == "EXIT":
        # prints biggest score
        exit()
    for line in quoteFile:
        quotes = line.split(";")
        if uinput == str(quotes[1]):
            gotRight = True
    if gotRight == False:
        print("This was incorrect!")
    else:
        print("CORRECT! well done")
        points += 1
    print(f"You have {points} points!")
    with open("scoreholder.txt", "a") as sH:
        sH.write(str(points) + "\n")
        sH.close()
    time.sleep(0.9)
    os.system("clear")
    
        
