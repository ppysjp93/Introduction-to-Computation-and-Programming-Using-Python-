print("################################################################################") 
print("""
EXAUSTIVE ENUMERATION""")
print("################################################################################") 

print("""
The code below prints the integer cube root if it exists. If the input given isn't
a perfect cube it prints a message to say tht this is the case.""")

print("""
x = int(input('Enter an integer: '))
ans = 0 
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else: 
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)\n""")
    
def CubeRootExist():
    x = int(input('Enter an integer: '))
    ans = 0 
    while ans**3 < abs(x):
        ans = ans + 1
    if ans**3 != abs(x):
        print(x, 'is not a perfect cube')
    else: 
        if x < 0:
            ans = -ans
        print('Cube root of', x, 'is', ans)

CubeRootExist()

print("\nDECREMENTING FUNCITION")

print("""
Whenever you write a while loop, you should think about an apporopriate 
decrementing function. This is a function that has the following properties.
\n* It maps a set of program variables into an integer
\n* When the loop is entered, its value is nonnegative.
\n* When its value is <= 0, the loop terminates
\n* Its value is decreased every time through the loop
\nIn the above program the Decrementing Functions is abs(x) - ans**3""")

print("""
The algorithmic technique used in the above program is called exhaustive 
enumeration. We enumerate all possibilities until we get to the right answer
or exhaust the space of possibilities. At first blush, this may seem like an 
incredibly stupid way to solve a problem. Surprisingly, however, exhaustive
enumeration algorithms are often the most pracical way to solve a problem.
They are typically easy to implement and easy to understand. And in many cases,
they run fast enough or all practical puposes. Try finding the cube root of 
1957816251""")

CubeRootExist()

print("""
Now try 7406961012236344616 a much larger example which the computer will still
manage to deal with without too much trouble.""")

CubeRootExist()

print("""
A modern computer can perform a single instruction which takes the order of one 
nanosecond to perform. In the time it takes for your voice to travel a hundred
feet, a modern computer can execute millions of instructions.""")

print("""
See how large the input needs to be before it is noticable the computer has to 
pause to print the output. (It's roughly 10000000)""")

print("""
maxVal = int(input('Enter a positive integer: '))
i = 0
while i < maxVal:
    i = i + 1 
print(i)""")

maxVal = int(input('Enter a positive integer: '))
i = 0
while i < maxVal:
    i = i + 1 
print(i)
