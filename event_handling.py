# Understanding Event Handlers in Python
# Money Laundering for the Mafia
# Tutorial by Angel Inokon
# Week 2: Intro to Interactive Programming
# 10.21.2012 v1

# Slides: http://tinyurl.com/wk2slidesmafia
# Code: http://www.codeskulptor.org/#user2-Wx1CXNf9nh-3.py

# Joe was a trusted money handler for The Boss.
# Follow this sample program to see
# event based programming in action.


# Import the definitions for the interface and events

import simplegui

# Global Variables

money_cleaned = 0
dialogue_1 = "THE BOSS:\t Hey Joey, I got somethin for ya.\n"
dialogue_2 = "JOE:\t\t How much do you need cleaned Boss?\n"
dialogue_3 = "JOE:\t\t It's all clean Boss...Here's $"
dialogue_4 = "\nTHE BOSS: \t That's my boy."
curr_dialogue = 1

# Helper Functions

def print_dialogue():
    if curr_dialogue == 1:
        print(dialogue_1 + dialogue_2)
    else:
        print (dialogue_3 + money_cleaned + dialogue_4)

# Event Handlers

def clean_money(money_stolen):
    # Only the handler knows the amount stolen.
    global curr_dialogue
    global money_cleaned
    money_cleaned = money_stolen
    curr_dialogue = 3
    print_dialogue()

def rob_bank():
    print_dialogue()

# Frame

frame = simplegui.create_frame("Clean Money", 100, 100)

# Register Event Handlers

"""When the enter key is pressed clean money will be called."""

frame.add_input("Money to be cleaned ", clean_money, 60)


# Start Frame and Game

rob_bank()
frame.start()
