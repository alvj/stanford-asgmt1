from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    put_first_beepers()

    # In worlds smaller than 3 columns wide front will not be clear. This prevents from crashing
    if front_is_clear():
        find_midpoint()
        # Moves Karel to the final position, standing in the beeper
        turn_around()
        move()
    

def put_first_beepers():
    """
    Karel places the first two beepers, on the last corner on each side of the row.

    Pre-condition: Karel is on the bottom left corner of the world, facing East.

    Post-condition: Karel is on the bottom right corner of the world, facing the opposite direction as it was before (West).
    """
    put_beeper()
    while front_is_clear():
        move()

    # Prevent from placing two beepers in one column worlds midpoint
    if no_beepers_present():
        put_beeper()
        turn_around()


def find_midpoint():
    """
    Karel moves two times to check if there is a beeper. If there is not a beeper, Karel keeps moving until it finds one, it picks it up and move it one step closer to the midpoint.
    If there is a beeper, it means that the midpoint is close, so Karel picks that beeper up and places it in the next corner (the midpoint).
    Then, Karel moves one step more to pick the last beeper which is not placed in the midpoint, so the only beeper left is the one placed in the midpoint.

    Pre-condition: Karel is standing in one of the two beepers next to a wall, facing away from the wall.

    Post-condition: Karel is one step away from the midpoint beeper, facing away from it. All the beepers that are not the midpoint one have been succesfully picked up by Karel.
    """
    while beepers_present():
        for i in range(2):
            move()
            
        if no_beepers_present():
            while no_beepers_present():
                move()
            move_beeper()
        else:
            move_beeper()
            move()
            pick_beeper()


def move_beeper():
    """
    Karel moves a beeper one step closer to the midpoint.

    Pre-contition: Karel is standing on a beeper, facing to the opposite direction from where it should be placed.

    Post-condition: Karel has moved the beeper and is now facing the opposite direction from what it was facing before.
    """
    pick_beeper()
    turn_around()
    move()
    put_beeper()


def turn_around():
    """
    Pre-condition: None.

    Post-condition: Karel is now facing the opposite direction from what it was facing before.
    """
    for i in range(2):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
