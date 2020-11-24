import time 
print("################################################################################") 
print("""
BISECTION SEARCH""")
print("################################################################################") 

print("""
Bisection search takes full advantage of the fact that numbers on a number line 
are ordered. In the same way that words in a dictionary are ordered 
lexicographical order, you can find a word in a dictionary very rapidly by 
making a guess at where you think the word is in the dictionary and then 
adjusting your guess again and again till you get to the word you are after.
Since number lines are 'ordered' we can make a stab at the value of the root of 
x. If the guess is too small we make a another guess which is between the guess
and some maximum value. And if the guess is too large we make another guess which
is less than the original guess and greater than 0. In both cases the new boundary
case is the "latest" guess. The code below will make sense of this paragraph:""")

print("""
def BisectionRoot(x):
    epsilon = 0.01
    numGuesses = 0 
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        print('low = ', low, 'high =', high, 'ans = ', ans)
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print('numGuesses =', numGuesses)
    print(ans, 'is close to square root of', x)""")

def BisectionRoot(x):
    epsilon = 0.01
    numGuesses = 0 
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        print('low = ', low, 'high =', high, 'ans = ', ans)
        numGuesses += 1
        if ans**2 < x:  
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
        time.sleep(1)
    print('numGuesses =', numGuesses)
    print(ans, 'is close to square root of', x, '\n')

print("""
x = 25 
BisectionRoot(x)\n""")

x = 25 
BisectionRoot(x)

print("""
x = -25 
BisectionRoot(x) don't do it because it causes an infinite loop\n""")

#x = -25 
#BisectionRoot(x)

