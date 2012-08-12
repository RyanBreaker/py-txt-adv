def go(direc):
    global x,y
    direcs = ["north",'n', "south",'s', "east",'e', "west",'w']
    diags  = ["northeast",'ne', "northwest",'nw', "southeast",'se', "southwest",'sw']
    if direc in direcs:
        if direc == direcs[0] or direc == direcs[1]:
            x += 1
        elif direc == direcs[2] or direc == direcs[3]:
            x -= 1
        elif direc == direcs[4] or direc == direcs[5]:
            y += 1
        elif direc == direcs[6] or direc == direcs[7]:
            y -= 1
        else:
            exit("ERROR: In go()")
    elif direc in diags:
        if direc == diags[0] or direc == diags[1]:
            x += 1
            y += 1
        elif direc == diags[2] or direc == diags[3]:
            x += 1
            y -= 1
        elif direc == diags[4] or direc == diags[5]:
            x -= 1
            y += 1
        elif direc == diags[6] or direc == diags[7]:
            x -= 1
            y -= 1
        else:
            exit("ERROR: In go()")
    else:
        if direc == "":
            print "Go where?"
        else:
            print "I have no idea where that is."
