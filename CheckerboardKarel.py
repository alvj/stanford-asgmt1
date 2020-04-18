from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    for i in range(8):
        fill_row()
        change_row()


def fill_row():
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()


def change_row():
    if facing_east():
        turn_left()
        move()
        turn_left()
    else:
        turn_right()
        move()
        turn_right()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
