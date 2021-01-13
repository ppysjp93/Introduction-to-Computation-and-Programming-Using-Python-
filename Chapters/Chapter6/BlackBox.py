print("################################################################################") 
print("""
BLACK BOX TESTING\n""")
print("################################################################################") 

print("""
Black-Box Testing allows testers and implementers to be drawn from separate
populations. Commericial Software is usually developed with quality assurance
groups who work largely independently of development groups. This independence
means that the code can be tested more rigourously. For example an implementer
might not test for negative integers when creating the isBigger function because
to them it is self evident that you wouldn't put a negative value into the
function. However a tester may stress the implemented code by putting a negative
value to see if the implementer has covered a wide range of scenarios. \n""")
 

print("""
Consider the following specification for a sqrt function for which we plan to
Black-Box Test:\n""")

def sqrt(x, epsilon):
    """
    Assumes x, epsilon floats
    x >= 0
    epsilon >= 0
    espilon > 0
    Returns result such that
    x - epsilon <= result*result <= x + espilon
    """

print("""
The BlackBox specification seems to only have 2 paths that need to be tested,
however it is clear that this isn't sufficient. It probably makes sense
especially when dealing with numbers to make sure that you test values along the
lines of the 7 subsets we looked at earlier.
It is importatnt to look at very small and very large values as well as typical
values. There is a nice table on page 88 that outlines a good 'test-suite' for
these values. Aliasing is a real threat so you must be aware of this as an issue
as you can see in the following code.""")

print('''
def copy(L1, L2):
    """
    Assumes L1, L2 are lists
    Mutates L2 to be a copoy of L1
    """
    while len(L2) >0: # remove all elements from L2
        L2.pop() #remove last element of L2
    for e in L1: # append L1's elemetns to intially empty L2
        L2.append(e)\n''')

print("""
This function works in the case that the lists L1 and L2 are different lists,
however if they both point to the same list then this won't work. If a test
suite didn't make the call copy(L, L) then this would not reveal the bug.\n""")


