print("################################################################################") 
print("""
SPECIFICATIONS """)
print("################################################################################") 

print("""
We are now going to generalise the bisection search by wrapping it in a function
called 'findRoot'. We are aso going to create a function that will testFindRoot
produces the expected result.""")

print('''
    def findRoot(x, power, epsilon):
        
        """Assumes x and epsilon int or float, power an int,
                epsilon > 0 & power >= 1
           Returns float y such that y**power is within epsilon of x.
                If such a float does not exist, it returns None"""

        if x < 0 and power%2 ==0: #Negative number has no even-powered roots
            return None

        low = min(-1.0, x)
        high = max(1.0, x)
        ans = (high + low)/2.0
        while abs(ans**power - x) >= epsilon:
            if ans**power < x:
                low = ans
            else:
                high = ans
            ans = (high + low)/2.0
        return ans

    def testFindRoot():
        epsilon = 0.0001
        for x in [0.25, -0.25, 2, -2, 8, -8]:
            for power in range(1,4):
                print('Testing x = ', str(x), ' and power = ', power)
                result = findRoot(x, power, epsilon)
                if result == None:
                    print('No root')
                else:
                    print('Root ~= ',result) 
                print()

testFindRoot()\n''')

def findRoot(x, power, epsilon):
    """Assumes x and epsilon int or float, power an int,
            epsilon > 0 & power >= 1
       Returns float y such that y**power is within epsilon of x.
            If such a float does not exist, it returns None"""
    if x < 0 and power%2 ==0: #Negative number has no even-powered roots
        return None

    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans

def testFindRoot():
    epsilon = 0.0001
    for x in [0.25, -0.25, 2, -2, 8, -8]:
        for power in range(1,4):
            print('Testing x = ', str(x), ' and power = ', power)
            result = findRoot(x, power, epsilon)
            if result == None:
                print('No root')
            else:
                print('Root ~= ',result) 
            print()

testFindRoot()

print("""
The findRoot function has its own doc string which is inside a pair of triple 
quotes. You can view the docstring by typing help(function). Try typing in the 
python interpreter help(abs). It will pull up its docstring.""")

print("\nSPECIFICATIONS")

print("""
So what exactly is a specification? A specifaction is a contract between the 
implementer of a function and those who will be writing programs that use the 
function. Those who use the function shall be referred to as 'clients'. There 
are 2 parts to this contract: 
    * Assumptions: Describe conditions that must be met by the client for the
        function to work. Acceptable types for each parameter and not infrequently
        constraints on the value of one or more of the parameters. 
    * Guarantees: Essentially is the expected behaviour of the function if 
        function has been called in such a way that it meets the assumptions.

Functions give us a way of creating computational elements that we can think of 
as primitives. The way they do this is through 'Decomposition' and 'Abstraction'.
    * Decomposition: Breaking a program into parts that are reasonably 
        self-contained and reusable in different settings
    * Abstraction: Hides detail. 'Does what it says on the tin' without knowing
        exactly how this is done. You don't need to know how a combustion engine
        works to be able to drive a car. Its a black box. It has been abstracted
        away from the user. It means we can use a piece of code without knowing
        its interior details, which we don't need to see, don't want to see and
        shouldn't even want to see. 
The true art of programming is finding the notion of relevance that is appropriate 
for both the bulder of an abstraction and the potential clients of the abstraction.
Abstraction is all about forgetting. 

    Teenager says: May I borrow the car tonight?

    Parent says: Yes, but be back before midnight, and make sure that the gas 
        tank is full.

    Teenager hears: Yes.
""")




