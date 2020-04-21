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
    return_to_start()

    # Karel checks if the right is clear so it can find the top wall and stop filling rows
    while right_is_clear():
        # If the row below starts with a beeper Karel does not have to do anything extra
        if beepers_present():
            reposition_next_row()
            fill_row()
            return_to_start()
        # If the row below starts with no beeper, Karel has to place a beeper in the first corner
        # of the next row
        else:
            reposition_next_row()
            put_beeper()
            if front_is_clear():
                move()
            fill_row()
            return_to_start()


def fill_row():
    """
    Karel checks if the front is clear so it can move forward and puts a beeper. Then checks again
    to see if it can move again, without placing a beeper. This creates the checkerboard pattern.
    Karel will loop this until it finds a wall.

    Pre-condition: Karel is on the left side of a row, facing East.

    Post-condition: Karel is at the end of the row, facing to the wall (East).
    Karel has placed a beeper every two rows.
    """
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()

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
