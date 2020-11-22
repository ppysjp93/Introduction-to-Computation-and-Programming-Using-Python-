def ReturnsNthRoot(integer, n):
    # Adapted from page 25 in book
    root = 0 
    while root**n < abs(integer): 
        root = root + 1
    if root**n != abs(integer):
        return
    else:
        if integer < 0:
            root = -root
        return root

integer = int(input('Enter an integer: '))
maxpwr = 5 
minpwr = 1

while minpwr < maxpwr: 
    minpwr = minpwr + 1
    root = ReturnsNthRoot(integer, minpwr)
    if root != None:
        print("root: {0} pwr: {1}".format(root, minpwr))
    else:
        print("No roots exist for pwr: {0}".format(minpwr))
 
