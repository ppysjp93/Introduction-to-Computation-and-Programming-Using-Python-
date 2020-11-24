print("################################################################################") 
print("""
BISECTION SEARCH""")
print("################################################################################") 

print("""
Imagine some asks you to write a program that find the square root of any none 
negative number. What should you do?
You should probably start by saying that you need a better problem statement.
For example, what should the program do if asked to find the square root of 2? 
The square root of 2 is not a rational number. Tis means that there is no way to 
precisely represent its value as a finite string of digits (or as a float), so 
the problem as initially stated cannot be solved.
The right thing to have asked for is a program that finds an approximation to 
the square root. We will return to this issue in considerable detail later in
the book. But for now, let's think of close enough as an answer that lies within 
some constant and call it epsilon of the actual answer.
The code below impments an algorithm that finds an approximation to a square
root. We are introduced to a new operator += which we have not previously used 
before.\n""")

print("""
x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs( ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses = {0}'.format(numGuesses))
if abs(ans**2 - x) >= epsilon:
    print("Failed on square root of", x)
else:
    print(ans, 'is close to square root of', x)\n""")

def SquareRoot(x):
    epsilon = 0.01
    step = epsilon**2
    numGuesses = 0
    ans = 0.0
    while abs( ans**2 - x) >= epsilon and ans <= x:
        ans += step
        numGuesses += 1
    print('numGuesses = {0}'.format(numGuesses))
    if abs(ans**2 - x) >= epsilon:
        print("Failed on square root of", x)
    else:
        print(ans, 'is close to square root of', x)

SquareRoot(25)

print("""
The key lesson you should learn from this example is that the methods of solving
a problem with a computer are often quite different from the methods that you 
would use if you were attempting to do so by hand.""")

print("""
If we try and find the square root of 0.25 we find that exhaustive enumeration
doesn't work. This is because the solution is outside the range 0 to x (Remember
for 0 < x < 1 the square rooot of x is GREATER than x, it flips. Zero to one 
world is a very strange place remember that).\n""")

SquareRoot(0.25)

print("""
One way to fix this is to upgrade the algorithm by changing the while statement
so that instead it is 
    while abs(ans**2 - x) >= epsilon and ans*ans <= x:
There are notes in the margins of the book to help understand this. You just
need to spend some time thinking about the fact that for abs(x) < 1
SquareRoot(x) > x. The initial implentation stops searching at ans <= x""")

print("""
def SquareRoot2(x, epsilon, n):
    step = epsilon**n
    numGuesses = 0
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and ans*ans <= x:
        ans += step
        numGuesses += 1
    print('numGuesses = {0}'.format(numGuesses))
    if abs(ans**2 - x) >= epsilon:
        print("Failed on square root of", x)
    else:
        print(ans, 'is close to square root of', x)""")

def SquareRoot2(x, epsilon, n):
    step = epsilon**n
    numGuesses = 0
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and ans*ans <= x:
        ans += step
        numGuesses += 1
    print('numGuesses = {0}'.format(numGuesses))
    print('abs(ans**2 - x) = {0}'.format(abs(ans**2 - x))) 
    if abs(ans**2 - x) >= epsilon:
        print("Failed on square root of", x)
    else:
        print(ans, 'is close to square root of', x)

print("""
If we let epsilon = 0.01 and n = 2, the same as before we now get: 
SquareRoot2(0.25, 0.01, 2)\n""")
SquareRoot2(0.25, 0.01, 2) 

print("""
The while loop will be executed roughly x/step times at most, where 
step = epsilon^n. The next example is with something much bigger
123456. \n
SquareRoot2(123456, 0.01, 2)""")

SquareRoot2(123456, 0.01, 2)

print("""
As you can see it fails to compute the answer. The reason for this is that the 
step size is too large. So to make it more accurate we can change the 2 to a 3 
and this will make the "chopping" even finer.Although now we it takes an age to
run! (In the script SquareRoot2 has been commented out for brevity.) \n 
SquareRoot2(123456, 0.01, 3)\n""")
# SquareRoot2(123456, 0.01, 3)

print("""
SquareRoot2(100, 0.01, 2)
SquareRoot2(10000, 0.01, 2)
SquareRoot2(1000000, 0.01, 2)
SquareRoot2(123456, 0.01, 2)""")

SquareRoot2(100, 0.01, 2)
SquareRoot2(10000, 0.01, 2)
SquareRoot2(1000000, 0.01, 2)
SquareRoot2(123456, 0.01, 2)

print("""
Why does the last one not work? It is much less than 1000000 clearly, at a guess
I would say it has something to do with some sort of strobing effect. Anyway 
moving on there is more to learn.""")



