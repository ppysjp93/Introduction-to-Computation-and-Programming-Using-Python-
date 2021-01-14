print("################################################################################") 
print('''
THINKING ABOUT COMPUTATIONAL COMPLEXITY\n''')
print("################################################################################") 

print('''
How should one go about answering the question "How long will the follwoing 
function take to run?" \n''')

print('''
def f(i):
    """
    Assume i is an int and i >= 0
    """
    answer = 1
    while i >= 1:
        answer *= i
        i -= 1
    return answer\n''')

def f(i):
    """
    Assume i is an int and i >= 0
    """
    answer = 1
    while i >= 1:
        answer *= i
        i -= 1
    return answer

print('''
We could run the program on some input and time it. But that wouldn't be
particularly informative because the result would depend upon
* the speed of the computer on which it is run,
* the efficiency of the Python implementation on that machine, and
* the value of the input.\n''')

print('''
We get around the first two issues by using a more abstract measure of time.
Instead of measuring time in milliseconds, we measure time in terms of the
number of basic steps executed by the program. 
For simplicity, we will use a random access machine as our model of computation.
In a random access machine, steps are executed sequentially, one at a time. A
step is an operation that takes a fixed amount of time, such as binding a
variable to an object, making a comparison, executing an arithmetic operation,
or accessing an object in memory. 
Now that we have a more abstract way to think about the meaning of time, we turn
to the question of dependence on the value of the input. We deal with that by
moving away from expressing time complexity as a single number and instead
relating it to the sizes of the inputs. This allows us to compare the efficiency
of two algorithms by talking about how the running time of each grows with
respect to the sizes of the inputs.
Of course, the actual running time of an algorithm depends not only upon the
sizes of the inputs but also upon their values. Consider, for example, the
linear search algorithm implemented by\n''')

print('''
def linearSearch(L, x):
    for e in L:
    if e ==x:
        return True
    return False\n''')

def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

print('''
Suppose that L is a list containing a million elements, and consider the call
linearSearch(L, 3). If the first element in L is 3, linearSearch will return
True almost immediately. On the other hand, if 3 is not in L, linearSearch will
have to examine all one million elements before returning False.
In general, there are three borad cases to think about:
    * The best-case running time is the running time of the algorithm when the
      inputs are as favorable as possible. I.e., the best-case running time is the
      minimum running time over all the possible inputs of a given size. For
      linearSearch, the best-case running time is independent of the size of L. 
    * Similarly, the worst-case running time is the maximum running time over
      all the possible iputs of a given size. For linearSearch, the worst-case
      running time is linear in the size of L.
    * By analogy with the definitions of the best-case and worst-case runnning
      time, the average-case (also called expected-case) running time is the
      average running time over all possible inputs of a given size.
      Alternatively, if one has some a priori information about the distribution
      of input values (e.g., that 90% of the time x is in L), one can tkae that
      into account\n''')

print('''
People usually focus on the worst case. All engineers share a common article of
faith, Murphy's Law: If something can go wrong, it will go wrong. The worst case
provides an upper bound on the running time. This is critical in situations
where there is a time constraint on how long a computation can take. It is not
good enough to know that "most of the time" the air traffic contrl system warns
of impending collisions before they occur.
Let's look at hte worst-case running time of an iterative implementation of the
factorial:\n''')

def fact(n):
    """
    Assumes n is natural number
    Returns n!
    """
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

print('''
The number of steps required to run this program is something like 2 (1 for the
intial assignment statement and 1 for the return) + 5n (counting 1 step for the
test in the while, 2 steps for the fist assignment statement in the
while loop, and 2 steps for the second assignment statement in the loop). So,
for exmaple, if n is 1000, the function will execute roughly 50002 steps. It
should be immediately obvious that as n gets large, worrying about the difference
between 5n and 5n + 2 is kind of silly. For this reason, we typically ignore
additive constants when reasoning about running time. Multiplicative constants
are more problematical. Should we care whether the computation takes 1000 steps
or 5000 steps? Multiplicative factors can be important. Whether a search engine
takes a half second or 2.5 seconds to service query can be the difference
between whether people that search engine or go to a competitor.\n''')

print('''
On the other hand, when one is comparing two different algorithms, it is often
the case that even multiplicative constants are irrelevant. Recall that in
Chapter 3 we looked at two algothims, exhaustive enumeration and bisection
search, for finding an approximation to the square root of a floaing point
number. Functions based on these algorithms are shown below:\n''')

print('''
def squareRootExhaustive(x, epsilon):
    """
    Assumes x and epsilon are positve floats & epsilon < 1
    Returns a y such that y*y is within epsilon of x
    """
    step = espilon**2
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and ans*ans <= x:
        ans += step
    if ans*ans > x:
        raise ValueError
    return ans\n''')

def squareRootExhaustive(x, epsilon):
    """
    Assumes x and epsilon are positve floats & epsilon < 1
    Returns a y such that y*y is within epsilon of x
    """
    step = espilon**2
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and ans*ans <= x: 
        # The ans*ans <= is there because of floating point arithmetic I think.
        ans += step                                         
    if ans*ans > x:
        raise ValueError
    return ans

print('''
def squareRootBi(x, epsilon):
    """
    Assumes x and epsilon are psoiive floats and epsilon < 1
    Returns a y such that y*y is within epsilon of x
    """
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans\n''')

def squareRootBi(x, epsilon):
    """
    Assumes x and epsilon are positive floats and epsilon < 1
    Returns a y such that y*y is within epsilon of x
    """
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        # Where as here the ans*ans <= x isn't required because every value in
        # the bisection search is by nature some factor of 2. Clever. 
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans

print('''
We saw that exhaustive enumeration was so slow as to be impractical for many
combinations of x and epsilon. For example, evaluating squareRootExhaustive(100,
0.0001) requires roughly one billion iterations of the while loop. In contrast,
evaluating squareRootBi(100, 0.0001) takes roughly twenty iterations of a
slightly more complex while loop. When the difference in the number of
iterations is this large, it doesn't really matter how many instructions are
in the loop. I.e. the multiplicative constants are irrelevant. \n''')
