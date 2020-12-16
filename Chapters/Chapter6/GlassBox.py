print("\nGLASS-BOX TESTING")

print("""
Consider the following code:\n""")

print("""
def isPrime(x):
    '''
    Assumes x is a nonnegative int
    Returns true if x is prime; False otherwise
    '''
    if x <= 2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True
\n""")

print("""
We can just see from the code that the values 0, 1 and 2 are being treated as
special cases. If you carefully look, its clear that this code will erroneously
return False for the case isPrime(2). Exploring all the possible paths in a
piece of code is well defined, and there are commercial tools which are designed
to objectively measure the completeness of glass-box tests. The aim of glass box
testing is to have a test-suite that is 'path-complete'. Depth of Recursion and
the number of times a loop is executed limit the possibility of reaching
'path-completion'. For example, the number of levels of recursion differs for a
recursive implementation of factorial, which means it is literally impossible to
check 'every' path because it changes for every value. 
Even if we have a path complete piece of code, not every bug will necessarily
have been exposed:\n""")

print('''
def abs(x):
        """
        Assumes x is an int
        Returns x if x>=0 and -x otherwise
        """
        if x < -1:
            return -x
        else:
            return x\n''')

print("""
You may be fooled into thinking thanks to the specification that you only need
to use a test-input that consists of 2 inputs say {2, -2} and that this would
suffice. The good thing about this test is that it covers 'all paths'. The only
problem is that abs(-1) returns -1. \n""")

print("\nGLASS BOX TESTING RULES OF THUMB")

print("""
* Test both branches of all if statements
* Make sure that each except clause is executed
* For each for loop, have test cases in which
    1) The loop is not entered (i.e. test on an empty list)
    2) The body of the loop is executed exactly once
    3) The body of the loop is executed more than once.
* For each while loop,
    1) Look at the same kinds of cases as when dealing with foor loops.
    2) Include test cases corresponding to all posible ways of exiting the loop.
        For example, for loop starting with
        while len(L) > 0 and not L[i] == e:
        find cases wher the loop exits because len(L) is greater than zero and
        cases where it exits because L[i] == e.
* For recursive functions, include test cases that cause the function to return
with no recursive calls, exactly one recursive call, and more than one recursive
call.\n""")

