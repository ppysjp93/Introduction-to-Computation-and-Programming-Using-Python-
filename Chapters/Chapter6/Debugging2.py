print("################################################################################") 
print("""
DESIGNING THE EXPERIMENT\n""")
print("################################################################################") 

print("""
Think of debugging as a search process, and each experiment as an attempt to
reduce the size of teh search space. One method could be to design an experiemnt
that can be used to decide whether a specific region of code is responsible for
a problem uncovered during integration testing. Another way to reduce the search
space is to reduce the amount of test data needed to provoke a manifestation of
a bug. 
Let's look at a contrived example to see how one might go about debugging it.
Imagine that you wrote the palindrome-checking code as follows: \n""")

print('''
def isPal(x):
    """
    Assumes x is a list
    Returns True if the list is a palindrome; False otherwise
    """
    temp = x
    temp.reverse
    if temp == x
        return True
    else:
        return False

def silly(n):
    """
    Assumes n is an int > 0
    Gets n inputs from user
    Prints 'Yes' if the sequence of inputs forms a palindrom;
        'No' otherwise
    """
    for i in range(n):
        result = []
        elem = input('Enter element: ') 
        result.append(elem)
        if isPal(result):
            print('Yes')
        else:
            print('No')
''')

def isPal(x):
    """
    Assumes x is a list
    Returns True if the list is a palindrome; False otherwise
    """
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False

def silly(n):
    """
    Assumes n is an int > 0
    Gets n inputs from user
    Prints 'Yes' if the sequence of inputs forms a palindrom;
        'No' otherwise
    """
    for i in range(n):
        result = []
        elem = input('Enter element: ') 
        result.append(elem)
        print(result) # Test Print 1
        if isPal(result):
            print('Yes')
        else:
            print('No')

print("""
If the code is really long you can implement a bisection search your self to
narrow down exactly where the problem is. All you have to do is devise a test
which will tell you which "half" the bug is occuring in and keep doing this on
repeat until you have narrowed down exactly where the bug is. For a terribly
long script of say a 1000 lines of code the worse case will be that it takes
about 10 sweeps to find exactly where your problem lies.\n""")


print("""
Test Print 1: Demonstrates that the result is not as expected. It looks as though
it is only ever a length of one. So to fix this if we move the result variable
outside the loop should fix this. Unfortunately we are still getting problems as
it still prints yes even when its not a palindrome. This means that the problem
we are looking for is most likely in side the isPal function. \n""")

def fixedSilly(n):
    """
    Assumes n is an int > 0
    Gets n inputs from user
    Prints 'Yes' if the sequence of inputs forms a palindrom;
        'No' otherwise
    """
    result = []
    for i in range(n):
        elem = input('Enter element: ') 
        result.append(elem)
        print("Test Print 1: ", result) 
        if isPal(result):
            print('Yes')
        else:
            print('No')


print("""
Again we pick somewhere "halfway", this time we are going to check halfway
through isPal at the if statement and see if temp and x and return the expected
values we are seaking. If we put in the array ['a', 'b'] into fixedIsPal we can
see that that both temp and x are ['a', 'b'] which isn't what we want. 
The problem we are encountering here is aliasing which is something that we have
been looking at earlier are in the book.\n""")

def fixedIsPal(x):
    """
    Assumes x is a list
    Returns True if the list is a palindrome; False otherwise
    """
    temp = x[:]
    temp.reverse()
    print("Test Print 2: temp {0}, x {1}".format(temp,x))
    if temp == x:
        return True
    else:
        return False

print("\nFINAL THOUGHTS")

print("""
Debugging can be done methodically and carefully. The bisection search is an
incredibly powerful tool that can be used to find exactly where the bug is
occuring. Below are a few pragmatic hints that should help when the debugging
gets tough. Check for the following: 
    * Passed arguments to a function in the wrong order,
    * Misspelled a name, e.g., typed a lowercase letter when you should have
        typed an uppercase one,
    * Failed t oreinitialize a variable
    * Tested that two flaoitng point values are equal instead of nearly equal
      (remember floating point arithmetic is not hte same as the arithmetic you
      learned in school)
    * Tested for value equality (e.g., compared two lists by writing the
        expression L1 == L2 when you mean object equality (e.g., id(L1) ==
            id(L2))
    * Forgotten that some built-in function has a side effect,
    * Forgotten the () that turns a reference to an object of type function
        into a function invocation
    * Created an unintention alias, or
    * Made any other mistake that is typial for you\n""")

print("\nPSYCHOLOGICAL ADVICE ")

print("""
1) Don't get in the habit of bullying yourself if the program is behaving
    unexpectedly.
2) Stop asking yourself why the program isn't doing what you want it to.
    Instead, ask yourself why it is doing what it is. This is an easier question
    to answer. 
3) Keep in mind that the bug is probably not where you think it is. A practical
    way of going about this is to ask where the bug cannot be. As Sherlock
    Holmes said, "Eliminate all other factors, and the one which remains must be
    the truth." 
4) Try to explain the problem to someone else. We all have blind spots which we
    develope, explaining it to someone else may reveal where you are going wrong.
    A good way to do this is to try and explain why the bug can't be in certain
    places. 
5) Don't believer everything you read. In particular, don't believe the
    documentation. The code may not be doing what the comments suggest. 
6) Stop debugging and start writing documentation. This will help you approach
    the problem from a different perspective. 
7) Walk away, and try again tomorrow. This may mean that bug is fixed later in
    time than if you had stuck with it, but you will probably spend a lot less of
    your time looking for it. That is, it is possible to trade latency for
    efficency.  \n""")

print("\nWHEN YOU HAVE FOUND THE BUG")

print("""
Before you make the change, try and understand the ramifications of the 'fix'
you propose. There is nothing more frustrating that implementing a fix and then
finding that it only makes initial problem worse! \n""")
