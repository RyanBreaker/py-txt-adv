#!/usr/bin/python2.7

import movement
import locations


def currLoc():
    """
    Prints current player location for debugging.
    """
    print "Current location: %d,%d" % (movement.x, movement.y)

currLoc()

### The actual game setup and loop starts here:
while True:
    # Get user input (ui).
    ui = raw_input('> ').lower()
    ui = ui.split(' ')
    ui.append(None)  # Prevent traceback.
    
    while ui[0] == '' and ui[1] is not None:
        # Remove any blanks, but leave one open to check.
        del(ui[0])

    if ui[0] == "go":
        movement.go(ui[1])
        currLoc()
        locations.checkLoc([movement.x, movement.y])
    elif ui[0] == "look":
        locations.checkLoc([movement.x, movement.y])
    elif ui[0] == "quit":
        exit("Bye!")
    else:
        if ui[0] != "":
            print "I don't understand that."
        else:
            pass
