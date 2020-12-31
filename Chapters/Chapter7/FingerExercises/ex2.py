print("################################################################################") 
print('''
FINGER EXERCISE\n''')
print("################################################################################") 

print('''
Implement a function that satisfies the specification\n''')

def findAnEven(L):
    """
    Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number
    """
    for val in L:
        if val % 2 == 0:
            return val 

    raise ValueError('L does not contain an even number')
