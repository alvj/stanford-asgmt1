from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    for i in range(3):
        fill_column()
        climb_down()
        move_to_next_column()
    # Fix fence post problem
    fill_column()


def fill_column():
    """
    Karel moves from the bottom to the top of the column, checking for the ceiling. Karel fills the missing beepers

    Pre-condition: Karel is at the bottom of the column, facing to the next column (East)

    Post-condition: Karel is at the top of the column whichever its height and it has filled all the missing beepers.
    Karel is facing to the ceiling (North)
    """
    turn_left()

    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        else:
            move()
    # Fix fence post problem
    if no_beepers_present():
        put_beeper()


def climb_down():
    """
    Karel goes back to the bottom of the column

    Pre-condition: Karel is at the top of a column facing to the ceiling

    Post-condition: Karel is at the bottom of the column whichever its height is. Karel is facing to the next column
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def move_to_next_column():
    """
    Karel moves from one finished column to the next one

    Pre-condition: Karel is at the bottom of a column facing to the next one

    Post-condition: Karel is at the bottom of the next column facing the same way it was before
    """
    for i in range(4):
        move()


def turn_around():
    """
    Makes Karel face the opposite way

    Pre-condition: None

    Post-condition: Karel is facing the opposite way it was facing before
    """
    for i in range(2):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
