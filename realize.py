def realize(coords):
    """
    "realize" = to find all of the coords inside an area
    Finds them by laying-out the coords in coordL/coordsR,
    getting the lowest and highest elements, and returning
    the possible coords.
    coords = [[2, 4],[6,4],[6,10],[2,10]]
    ###    Left^  ^Right
    """
    coordsL = [] # Left  coords Laid-out
    coordsR = [] # Right coords Laid-out
    for i,j in coords: # for each list in coords list:
        coordsL.append(i) # append first
        coordsR.append(j) # append right
    
    if len(coordsL) == 2: # checking if 2 or 4 points were given
        h = 1
    elif len(coordsL) == 4:
        h = 3
    else:
        exit("ERROR")
    coordsL.sort()  # Sort to get lowest and highest easily
    lL = coordsL[0] # lowest-left
    hL = coordsL[h] # highest-left
    coordsR.sort()
    lR = coordsR[0]
    hR = coordsR[h]
    
    if lL > hL or lL == hL: # sanity check
        exit("ERROR: In realize") # Need to work on better error messages
    elif lR > hR or lR == hR:
        exit("ERROR: In realize")
    
    coords = [] # resetting coords list to accept new values
    lRr = lR # low-Right reset
    while lL <= hL:
        while lR <= hR:
            coords.append([lL,lR])
            lR += 1
        lL += 1
        lR = lRr
    
    return coords
