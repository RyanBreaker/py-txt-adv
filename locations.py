import messages
import movement
# Define your locations below this function definition


def realize(ty, coords):
    """
    "realize" = to find all of the coords inside an area
    Finds them by laying-out the coords in coordX/coordsY,
    getting the lowest and highest elements, and returning
    the possible coords.
    There are two modes:
        1: Finds each coordinate within the area
        2: Finds just the coordinates of the edges of the area
    coords = [[2, 4],[6, 4]]
    ###       X^  ^Y
    """
    coordsx = []
    coordsy = []
    for i, j in coords:
        coordsx.append(i)  # append left
        coordsy.append(j)  # append right

    # checking if 2 or 4 points were given
    if len(coordsx) == 2:
        h = 1
    elif len(coordsx) == 4:
        h = 3
    else:
        exit("ERROR")
    coordsx.sort()   # Easily getting lowest and highest
    lx = coordsx[0]  # lowest-X
    hx = coordsx[h]  # highest-X
    coordsy.sort()
    ly = coordsy[0]  # same for y
    hy = coordsy[h]

    if lx > hx or lx == hx:  # sanity check
        exit("ERROR: In realize")  # Need to work on better error messages
    elif ly > hy or ly == hy:
        exit("ERROR: In realize")

    # resetting coords list to accept new values
    coords = []
    if ty == 1:
        lyr = ly   # low-Right reset
        while lx <= hx:
            while ly <= hy:
                coords.append([lx, ly])
                ly += 1
            lx += 1
            ly = lyr
    elif ty == 2:
        # Goes around the edges of the area.
        for x in range(lx, hx + 1):
            coords.append([x, ly])
        for y in range(ly, hy + 1):
            coords.append([hx, y])
        for x in range(hx, lx - 1, -1):
            coords.append([x, hy])
        for y in range(hy, ly - 1, -1):
            coords.append([lx, y])

    return coords

###################################
# Define borders for locations here
# Use only square coordinates for now
# Either all 4 points or 2 diagonal corners can be used
# All areas shall be defined and entered into the realize() function here
forest1 = [[0, 5], [5, 10]]
bigTree1 = [[3, 7]]

forest1Outline = realize(2, forest1)
forest1 = realize(1, forest1)


def Fforest1(xy):
    print messages.forest1_travel
    if xy in bigTree1:
        print messages.bigTree1


def checkLoc(xy):
    """
    Simply checks if the player is within an area and will call the
    appropriate function as needed.
    """
    print xy
    print forest1
    #xy = [[movement.x, movement.y]]
    if xy in forest1:
        Fforest1(xy)
    #del(xy)
