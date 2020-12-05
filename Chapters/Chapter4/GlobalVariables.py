print("################################################################################") 
print("""
GLOBAL VARIABLES""")
print("################################################################################") 
 
print("""
Imagine a recursive function and you want to know how many recursive calls have
been made. One way to do this is by using global variable. Let's consider the
Fib function from earlier: """)

def fib(x):    
    """Assumes x an int >= 0
       Returns Fibonacci of x"""  
    global numFibCalls
    numFibCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def testFib(n):
    for i in range(n+1):
        global numFibCalls
        numFibCalls = 0 
        print('fib of', i, '=', fib(i))
        print('fib called', numFibCalls, 'times.')

testFib(6)

print("""
Global variables are sometimes necessary but on the whole it is best to try and
avoid using them because they become sloppy quickly and destroy the locality of
a programme. """)
