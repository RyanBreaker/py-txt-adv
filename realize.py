# [0,0] [5,0] [5,5] [0,5]
# Would include:
#   [0,0],[0,1],[0,2],[0,3],[0,4],[0,5]
#   [0,0],[1,0],[2,0],[3,0],[4,0],[5,0]
#   		

def realize(coords):
	"""
	"realize" = to find all of the coords inside an area
	Finds them by laying-out the coords in coordL, getting the
	lowest and highest elements, and returning the possible
	coords
	"""
    e = 0 # element number
    coordsL = [] # Coords 'Laid'-out
    for i in coords: # lays out coords to get lowest/highest nums
		for ii in coords[e]:
			coordsL.append(ii)
		e += 1
	
    coordsL.sort()
    l = coordsL[0] # lowest
    h = coordsL[7] # highest
    
    if l > h or l == h: # sanity check
		exit("ERROR: In realize")
	
	# adding more Saturday
