'''
Reference:

Add to a set: myset.add(item)

Check if a something is in a set: 
if item in myset:
    do_stuff
else ...
'''
#Awesome Ban System
f = open(".ban.txt", "a+")
f.write("")
f.close

import sys
import random
from random import randint
from random import choice
import board

used = set()


def generate_numb():
    numb = random.randint(1, 75)
    return numb

def sort_numb(numb):
    if 1 <= numb <= 15:
        letter = 'B'
    elif 16 <= numb <= 30:
        letter = 'I'
    elif 31 <= numb <= 45:
        letter = 'N'
    elif 46 <= numb <= 60:
        letter = 'G'
    else:
        letter = 'o'
    numb = str(numb)
    comb = letter+numb
    return comb

def call_comb(comb):
    print("---" *7)
    print("Your Number Was " + comb)
    print("---" *7)
    print("")

def program(): #The main code of the Bingo Generator will be kept here
    spammer = True # Just for now
    cheater = False # Just for now
    count = 1
    while len(used) < 75:
        numb = generate_numb()
        comb = sort_numb(numb)
        if comb in used:
            continue
        else:
            used.add(comb)
            call_comb(comb)
        print("Press Enter to Continue")
        print("Press 'bingo' to Win and Go Back to the Main Menu")
        print("---" *7)
        keyboard_choice = input()
        if keyboard_choice == '':
            print(len(used))
            count += 1
            continue
        elif keyboard_choice == 'bingo':
            if count <= 4:
                cheater = True # Need at least 4 numbers to win (freespace)
                spammer = False # Cheater, not a Spammer
                break # Bad stuff will happen...
            else:
                spammer = False
                break
        else:
            print("Invalid Choice")
            print("Exiting...")
            sys.exit(0)

    if spammer:
        print("Stop Spamming!")
        print("Since you are obviously using this program just to spam, it will exit now, and also ban you...")
        f = open(".ban.txt", 'w')
        f.write("yep")
        f.close
        sys.exit(0)
    elif cheater:
        print("---" *7)
        print("CHEATER!")
        print("Being Annoying Because CHEATERS NEVER WIN!")
        f = open(".ban.txt", 'w')
        f.write("yep")
        f.close
        sys.exit(0)
    else:
        print("---" *7)
        menu()

# Menu
def menu(): #For Restarting
    print("Hello and Welcome to the Bingo Caller/Generator")
    print("Please choose one of the options below, then click enter")
    print("")
    print("1) Start The Program")
    print("2) Generate a Board")
    print("3) Exit the Program")
    print("---" *7)
    keyboard_choice = input()
    if keyboard_choice == '1':
        print("---" *7)
        program()
    if keyboard_choice == '2':
        keyboard_choice = input("Please enter the number of boards you need ")
        try:
            keyboard_choice = int(keyboard_choice)
        except ValueError:
            print("What you entered was not a number or was a decimal")
            print("Exiting...")
            sys.exit(0)
        board.main(keyboard_choice)
        menu()
    if keyboard_choice == '3':
        sys.exit(0)

f = open(".ban.txt", "r")
if "yep" in f:
    print("You Got Banned")
    print("(**oof)")
    f.close
    sys.exit(0)
else:
    menu()