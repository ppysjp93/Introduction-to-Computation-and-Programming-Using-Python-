numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
# Concatenate X toPrint numXs times
while numXs > 0:
    toPrint = toPrint + 'X'
    numXs = numXs - 1
print(toPrint)
