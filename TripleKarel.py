from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    for i in range(2):
        paint_building()
        reposition_different_building()
    # Painting last building out of the for loop prevents from a fence post error
    paint_building()


def paint_wall():
    """
    Checks if there is a wall and places a beeper in each corner of the wall
    while moving towards the other side of the wall

    Pre-condition: Karel is next to a wall and is facing parallel to the wall, towards the end of it

    Post-condition: Karel is at the end of the wall with a beeper in each corner
    facing the same way it was facing before
    """
    while left_is_blocked():
        put_beeper()
        move()


def paint_building():
    """
    Karel paints all three walls of a building.

    Pre-condition: Karel is positioned next to the start of the first wall, facing towards the end of it.

    Post-condition: Karel has moved to the last wall of the building that needed to be painted,
    painting all the walls as it moved.
    """
    for i in range(2):
        paint_wall()
        reposition_same_building()
    # Painting last wall out of for loop fixes fence post problem
    paint_wall()


def reposition_same_building():
    """
    Moves from the end of one wall to the start of the next one in the same building so it can be painted.

    Pre-condition: Karel is positioned immediately at the end of a wall, facing away from it.

    Post-condition: Karel is positioned at the start of the next wall, facing towards the end of it,
    matching the pre-condition on paint_wall().
    """
    turn_left()
    move()


def reposition_different_building():
    """
    Karel is next to the first wall of the next building facing the right direction.

    Pre-condition: Karel is facing right to the wall of the next building.

    Post-condition: Karel now faces to the right of what it was facing previously, aligned to the first wall of the
    next building.
    """
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
