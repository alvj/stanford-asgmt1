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
    fill_row()
    while right_is_clear():
        if beepers_present():
            reposition_next_row()
            fill_row()
        else:
            reposition_next_row()
            put_beeper()
            if front_is_clear():
                move()
            fill_row()


def fill_row():
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()
    return_to_start()

def reposition_next_row():
    """
    Karel moves to the row that is directly above.

    Pre-condition: Karel is facing to the wall (West).

    Post-condition: Karel is facing away from the wall (East) and is in the row above.
    """
    turn_right()
    move()
    turn_right()


def return_to_start():
    """
    Karel goes back to the start of the row.

    Pre-condition: Karel is at the end of the row, facing to the wall.

    Post-condition: Karel is now at the start of the same row
    """
    turn_around()
    while front_is_clear():
        move()


def turn_around():
    """
    Pre-condition: None

    Post-condition: Karel is now facing to the opposite direction of what it was facing before
    """
    turn_left()
    turn_left()


def turn_right():
    """
    Pre-condition: None

    Post-condition: Karel is now facing to the right of whichever direction it was facing before
    """
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
