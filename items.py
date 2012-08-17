inventory = {}
#items = {'apples': 100}

#print items['apples']


try:
    inventory['apples'] += 1
except KeyError:
    inventory['apples'] = 1

print inventory['apples']

"""
Items:
    Unique: Can only make one of each item; location set in key's tuple.
    Common: Can have many; no location set but can have multiple in an area.
            If a common item is moved and dropped, It will be relabled as an
            Unique item.
"""
