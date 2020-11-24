print("################################################################################") 
print("""
FINGER EXERCISE PAGE 34 """)
print("################################################################################") 

import time
 
def CubeRoot(x):
    epsilon = 0.01
    numGuesses = 0 
    #low = 0.0
    low = min(x, 0.0)     # this is my guess to make negatives work
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**3 - x) >= epsilon:
        print('low = ', low, 'high =', high, 'ans = ', ans)
        numGuesses += 1
        if ans**3 < x:  
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
        time.sleep(1)
    print('numGuesses =', numGuesses)
    print(ans, 'is close to cube root of', x, '\n')


x = -27
CubeRoot(x)
