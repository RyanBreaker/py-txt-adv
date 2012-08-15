def limit(ty):
    """
    Checks if the player can move somewhere and not outside of
    the game world.
    ty = type
    ty 1 = check if x can ++ (North)
    ty 2 = check if x can -- (South)
    ty 3 = check if y can ++ (East)
    ty 4 = check if y can -- (West)
    """
    # Define X,Y minimums and maximums here:
    x_max = 10
    x_min = 0
    y_max = 10
    y_min = 0

    if ty == 1:
        if x + 1 > x_max:
            return False
        else:
            return True
    elif ty == 2:
        if x - 1 < x_min:
            return False
        else:
            return True
    elif ty == 3:
        if y + 1 > y_max:
            return False
        else:
            return True
    elif ty == 4:
        if y - 1 < y_min:
            return False
        else:
            return True
    else:
        exit("ERROR: In limit.")


def go(direc):
    """
    The player-entered 'go' function.
    If the player entered go, the second arg is passed as direc
    and the player can move in such directions as listed below.
    """
    global x, y
    direcs = ["north", 'n', "south", 's',
              "east", 'e', "west", 'w']
    diags = ["northeast", 'ne', "northwest", 'nw',
             "southeast", 'se', "southwest", 'sw']
    if direc in direcs:
        if direc == direcs[0] or direc == direcs[1]:
            # North
            if limit(1):
                x += 1
            else:
                print "Cannot go that far North!"  # will make error better
        elif direc == direcs[2] or direc == direcs[3]:
            # South
            if limit(2):
                x -= 1
            else:
                print "Cannot go that far South!"
        elif direc == direcs[4] or direc == direcs[5]:
            # East
            if limit(3):
                y += 1
            else:
                print "Cannot go that far East!"
        elif direc == direcs[6] or direc == direcs[7]:
            # West
            if limit(4):
                y -= 1
            else:
                print "Cannot go that far West!"
        else:
            exit("ERROR: In go()")
    elif direc in diags:
        if direc == diags[0] or direc == diags[1]:
            # NorthEast
            if limit(1) and limit(3):
                x += 1
                y += 1
            else:
                print "Cannot go NorthEast!"
        elif direc == diags[2] or direc == diags[3]:
            # NorthWest
            if limit(1) and limit(4):
                x += 1
                y -= 1
            else:
                print "Cannot go NorthWest!"
        elif direc == diags[4] or direc == diags[5]:
            # SouthEast
            if limit(2) and limit(3):
                x -= 1
                y += 1
            else:
                print "Cannot go SouthEast!"
        elif direc == diags[6] or direc == diags[7]:
            # SouthWest
            if limit(2) and limit(4):
                x -= 1
                y -= 1
            else:
                print "Cannot go SouthWest!"
        else:
            exit("ERROR: In go()")
    else:
        if direc == "":
            print "Go where?"
        else:
            print "I have no idea where that is."

# Set player starting-point here.
x = 0
y = 0
