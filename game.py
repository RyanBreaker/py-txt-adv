import messages
import movement
# Import all areas after checkIn
from locations import checkLoc, forest1

def currLoc():
    """
    Prints current player location for 
    debugging.
    """
    print "Current location: %d,%d" % (movement.x, movement.y)


### The actual game setup and loop starts here
print "Loading..."

#currLoc()

while True:
    # Get user input (ui).
    ui = []  # reset ui
    ui = raw_input('> ')
    ui = ui.split(' ')
    ui.append("")  # prevent traceback

    if ui[0] == "go":
        movement.go(ui[1])
        #currLoc()
    elif ui[0] == "quit":
        exit("Bye!")
    else:
        if ui[0] != "":
            print "I don't understand that."

    # Check location
    loc = checkLoc()
    
    if loc == 'forest1':
        print messages.forest1_travel
