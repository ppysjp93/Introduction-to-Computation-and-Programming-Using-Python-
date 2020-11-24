print("################################################################################") 
print("""
NEWTON-RAPHSON""")
print("################################################################################") 

print("""
The Newton-Raphson algorithm is used to find the real roots of many functions,
we shall look at it in the context of only one variable. A polynomial with one
variable is either 0 or the sum of finte number of nonzero terms like 3x^2 + 2^x 
+ 3. Each term has a coefficient and a variable raised to some exponent. The
exponent on a variable is called the degree of that term. The degree of a 
polynomial is the largest degeree of any single term. In the example above the
degree is 2 (3x^2). 
If we have a polynomial p and r a real number, we write p(r) to stand for the
value of the polynomial when x = r. A root of the polynomial p is a solution to
the equation p = 0. such that p(r) = 0. Finding an approximation for the square 
root of 24 can be formulated as finding an x such that x^2 - 24 ~ 0.
Newton proved that if you guess the root and call it 'g' which is an
approximation for r then the next guess can be calculated with the following 
equation: 
    g = g - p(g)/p'(g) 
Where p'(g) is the derivative of p at g. Below is an implementation of the
Newton-Raphson algorthm for finding the square-root of 24.\n""")

print("""
epsilon = 0.01
k = 24.0
guess = k / 2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
print('Square root of', k, 'is about', guess)""")

epsilon = 0.01
k = 24.0
guess = k / 2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
print('Square root of', k, 'is about', guess)

def BisectionRoot(x):
    epsilon = 0.01
    numGuesses = 0 
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        numGuesses += 1
        if ans**2 < x:  
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print('numGuesses for BisectionRoot =', numGuesses)
    print('Square root of', x, 'is about', ans)

print()

def NewtonRaphson(k):
    epsilon = 0.01
    guess = k / 2.0
    numGuesses = 0 
    while abs(guess*guess - k) >= epsilon:
        numGuesses += 1
        guess = guess - (((guess**2) - k)/(2*guess))
    print('numGuesses for NewtonRaphson =', numGuesses)
    print('Square root of', k, 'is about', guess)

print("""
We are now going to comparet the efficiency of the Bisection Search, which 
by the way is logarithmic in the amount of operations it requires to find the 
square root. So it is pretty damn good already and see how much more efficient
the Newton Raphson is.\n""")

x = 24
BisectionRoot(x)
NewtonRaphson(x)

x = 1029394
BisectionRoot(x)
NewtonRaphson(x)

x = 1123412342345352029394
BisectionRoot(x)
NewtonRaphson(x)
