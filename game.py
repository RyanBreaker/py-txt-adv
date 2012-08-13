### The actual game setup and loop
print "Loading..."

import locations
import movement

### Insert other starting imports and stuff later

print "Current location: %d,%d" % (movement.x, movement.y)

while True:
    # Get user input (ui).
    ui = [] # reset ui
    ui = raw_input('> ')
    ui = ui.split(' ')
    ui.append("") # prevent traceback
    if ui[0] == "go":
        movement.go(ui[1])
        print "Current location: %d,%d" % (movement.x, movement.y)
    elif ui[0] == "quit":
        exit("Bye!")
    else:
        print "I don't understand that."
