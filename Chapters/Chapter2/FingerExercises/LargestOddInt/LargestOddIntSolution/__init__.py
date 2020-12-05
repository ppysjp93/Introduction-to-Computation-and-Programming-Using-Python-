def IsOdd(integer):
    """
    IsOdd returns True if an odd integer is passed as its argument and 
    returns False if an even integer is passed as its argument. If 
    anything but an integer is passed an InvalidArgumentException is called.
    """
    if integer % 2 == 1:
        return True
    else:
        return False


def LargestOf2(a, b):
    """
    LargestOf2 returns the largest value of 2 integers
    """
    if a > b: 
        return a
    else:
        return b

def LargestOf3(a, b, c):
    """
    LargestOf3 returns the largest value of 3 integers
    """
    return LargestOf2(LargestOf2(a, b), c)

def LargestOdd(x, y, z):
    """
    returns the largest odd number from the 3 variables. 
    If none of them are odd an ArithmeticErroris raised.
    """
    if IsOdd(x) and IsOdd(y) and IsOdd(z): 
        return LargestOf3(x, y, z)
    elif IsOdd(x) and IsOdd(y):
        return LargestOf2(x, y)
    elif IsOdd(x) and IsOdd(z):
        return LargestOf2(x, z)
    elif IsOdd(y) and IsOdd(z):
        return LargestOf2(y, z)
    elif IsOdd(x):
        return x
    elif IsOdd(y):
        return y
    elif IsOdd(z):
        return z
    else:
        raise ArithmeticError("One Argument must be Odd")
    
