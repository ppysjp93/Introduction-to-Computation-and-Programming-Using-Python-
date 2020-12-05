print("################################################################################") 
print("""
INTRODUCTION""")
print("################################################################################") 

print("""
So far we have only been dealing with scalar data types and strings. In this 
chapter we are going to focus on data structures which are more non-scalar, in
particular tuple, list, range and dict.""")

print("\nTUPLES")

print("""
Like strings, tuples area immutable ordered sequences of elements. The
difference is that the elements of a tuple need not be characters. The
individual elements can be any type, and need not be of the same type as each
other. Literals of type tuple are written by enclosing a comma-separated list of
elements within parentheses. For example, we can write""")

print("""
t1 = ()
t2 = (1, 'two', 3)
print(t1)
print(t2)
""")

t1 = ()
t2 = (1, 'two', 3)
print(t1)
print(t2)

print("""
Since parentheses are used to group expressions (1) is a verbose way of writing
the integer 1. So to denote the singleton tuple containing this value, we write
(1,). Almost everyone that writes in python has at some stage ommitted the comma
so try and avoid being tricked into this mistake.""")

print("""
Repitition can be used on tuples like in the example below:
a = 3*('a', 2)""")

a = 3*('a', 2)
print("\na = \n", str(a))

print("""
t1 = (1, 'two', 3)
t2 = (t1, 3.25)
print(t2)
print(t1 + t2)
print((t1 + t2)[3])
print((t1 + t2)[2:5]) \n""")

t1 = (1, 'two', 3)
t2 = (t1, 3.25)
print(t2)
print(t1 + t2)
print((t1 + t2)[3])
print((t1 + t2)[2:5]) 

print("""
As you can see, tuples can be concatenated, indexed and sliced. t2 is an
interesting assignment because it assigns itself to the t1 tuple and the float
3.25. This is possible because like everything in pyton, a tuple is an object,
so tuples can contain tuples.""")

print('''
def intersect(t1,t2):
    """Assumes t1 and t2 are tuples
       Returns a tuple containing elements that are in
       both t1 and t2"""
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result''')

def intersect(t1,t2):
    """Assumes t1 and t2 are tuples
       Returns a tuple containing elements that are in
       both t1 and t2"""
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result

print("\nSEQUENCES AND MULTIPLE ASSIGNMENT")

print("""
Python has a multiple assignment statement system to etract individual elements
like: 
x, y = (3, 4)""")

x, y = (3, 4)
print("\nx = \n", str(x))
print("\ny = \n", str(y))

print("""
We can also do the same thing with strings so:
a, b, c ='xyz' which will bind a to 'x', b to 'y' and c to 'z'""")

a, b, c = 'xyz'
print("\na = \n", str(a))
print("\nb = \n", str(b))
print("\nc = \n", str(c))

print("""
This mechanism comes in handy especially when we have a function that returns 
fixed-size sequences. Consider the following:""")

print('''
def findExtremeDivisors(n1, n2):
    """
    Assumes that n1 and n2 are positive ints
    Returns a tuple containing the smallest common divisor > 1 and the largest
    common divisor of n1 and n2. If no common divisor, other than 1, returns
    (None, None)
    """
    minVal, maxVal = None, None
    for i in range(2, min(n1,n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return(minVal, maxVal)''')

def findExtremeDivisors(n1, n2):
    """
    Assumes that n1 and n2 are positive ints
    Returns a tuple containing the smallest common divisor > 1 and the largest
    common divisor of n1 and n2. If no common divisor, other than 1, returns
    (None, None)
    """
    minVal, maxVal = None, None
    for i in range(2, min(n1,n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return(minVal, maxVal)

print("""
minVal, maxVal = findExtremeDivisors(100,200) """)

minVal, maxVal = findExtremeDivisors(100,200) 
print("\nminVal = \n", str(minVal))
print("\nmaxVal = \n", str(maxVal))

print("""
I like this algorithm a lot. It's very succinct.""")
