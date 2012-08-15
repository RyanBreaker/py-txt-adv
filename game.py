from movement import go, x, y
#from locations import checkIn

### The actual game setup and loop starts here
print "Loading..."

### Insert other starting imports and stuff later

print "Current location: %d,%d" % (x, y)

while True:
    # Get user input (ui).
    ui = []  # reset ui
    ui = raw_input('> ')
    ui = ui.split(' ')
    ui.append("")  # prevent traceback
    if ui[0] == "go":
        go(ui[1])
        print "Current location: %d,%d" % (x, y)
    elif ui[0] == "quit":
        exit("Bye!")
    else:
        print "I don't understand that."
