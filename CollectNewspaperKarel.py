from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    walk_to_newspaper()
    pick_beeper()
    walk_to_initial_position()


def walk_to_newspaper():
    """
    Makes Karel move out of the house and to the newspaper.

    Pre-condition: None.

    Post-condition: Karel is in the same corner as the newspaper.
    """
    turn_right()
    move()
    turn_left()
    for i in range(3):
        move()


def walk_to_initial_position():
    """
    Makes Karel move to its initial position.

    Pre-condition: Karel is in the same corner as the newspaper and it is facing East.

    Post-condition: Karel has to be in its initial position in the upper left corner of the house.
    """
    turn_around()
    for i in range(3):
        move()
    turn_right()
    move()


def turn_around():
    """
    Makes Karel face to the opposite direction by turning left two times.

    Pre-condition: None.

    Post-condition: Karel is facing the opposite way from what it was facing before.
    """
    for i in range(2):
        turn_left()


def turn_right():
    """
    Karel turns to the right by turning left three times.

    Pre-condition: None.

    Post-condition: Karel is facing right of whichever direction was facing previously
    """
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
