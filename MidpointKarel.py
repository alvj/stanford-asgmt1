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
    turn_around()
    find_midpoint()
    turn_around()
    move()

def put_first_beepers():
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()


def find_midpoint():
    while beepers_present():
        move()
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
    pick_beeper()
    turn_around()
    move()
    put_beeper()


def turn_around():
    for i in range(2):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
