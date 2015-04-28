#!/usr/bin/python

import sys

"""
Taken from SO: /questions/3041986/python-command-line-yes-no-input
Converts y to True
Converts n to False
"""
### THIS WHOLE SECTION IS BROKEN... and i dont know why
def usr_yn(question):
    sys.stdout.write('%s [y/n]\n' % question)
    choice = raw_input().lower
    yes = ["y",'yes','ye','']
    no = ['n','no']
    if choice in yes:
        return True
    if choice in no:
        return False
    else:
        sys.stdout.write("Please respond with 'y'es or 'n'o\n")
"""
A way to tell players they are dead, and why they died on a new line!
Also, a way for them to exit the script OR to continue playing again!
This needs to function well, players will be seeing this alot!
# Wondering if i should break Continue into a seperate section #
"""
def dead(why):
    print why, "Congratz! You Are Dead!\n"
    usr_yn("Would you like to try again?")

    if True:
        start_bedroom()
    else:
        exit(0)

"""
Asks the user to press enter before continueing,
Partially Taken from SO: /questions/3084508/clear-terminal-in-python
Should work in both Py2.X and 3.x
\x1b[ starts a command
2J clears the screen H (with no args) returns the cursor to the top left # Port this to other OS's? This is only suppored in ANSI # """
def clear():
    raw_input("Press Enter To Continue")
    sys.stderr.write("\x1b[2J\x1b[H")
