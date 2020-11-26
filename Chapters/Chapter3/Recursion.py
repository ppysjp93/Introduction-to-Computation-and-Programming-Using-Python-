print("################################################################################") 
print("""
RECURSION""")
print("################################################################################") 

print("""
 A recursive function is made up of two parts. It has a base case that directly
specifies the result for a special case. And there is a recursive case (aka
inductive case) that defines the answer in terms of the of the answer to the
question on some other input, typically a simpler version of the same problem. 

Factorials lend themselves to being defined recursively. The first function
defined below is the iterative form of the factorial function followed by its
recursive sister.""")

print('''
def FactR(n):
    """Assumes n an int > 0
        Returns n!"""
    if n == 1:
        return n
    else:
        return n*factR(n-1)''')

print("""
You can see that it the iterative form is simple enough but not the most
intuitve to read. Now look at its recursive brother: """)

print('''
def FactR(n):
    """Assumes n an int > 0
        Returns n!"""
    if n == 1:
        return 1
    else:
        return n*FactR(n-1)''')

print("\nFIBONACCI NUMBERS")

print("""The fibonnaci sequence is another function that is commonly defined recursively.
Fibonacci was an Italien mathematician who developed the formula in 1202.
Although the sequence was discovered earlier by the Sanskrit mathematician
Pingala. Fibonnaci noticed the sequence cropped up when considering rabbit
populations with some unrealistic assumptions. 
    * A new pair of newly born rabbits are put in a pen
    * They are able to mate after one month
    * It takes one month for the babies to gestate
    * The female always produces a new pair of rabits from its second month on.
    * No rabbits ever die 
What is the population of rabbits after 6 months? 

On the last day of the first month there will be one female. On the last day of
the second month there will be 1 female still, ready to give birth the next day. 
On the last day of the third month there will be 2 females (The original female 
 will have finally given birth). On the last day of the 4th month there will be 
3 females (the original female gives birth again!). On the last day of
the 5th month there will be 5 females ( the orignal female gives birth, the 
female born in the third will gives birth also from now on). On the last day of 
the 6th month the will be 8 females (the original female, female from third 
month, female from 4th month all now give birth from now on). And so on... 

So far I have described the passing of 5 full months so one more iteration will
give us the number of female rabbits after 6 months which is 13. Not bad aye for
some broody rabbits!""") 

print("""
Note the base cases and the recurrence relation if n represents the number of
months past: 

    females(0) = 1 
    females(1) = 1
    females(n) = females(n-1) + females(n-2)""")

print("""
This function is more 'expensive' as it makes 2 recursive calls for the
recursive case which is worht noting. Below is the coded form for the fibonnaci
function""")

print("""
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)\n""")

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('fib of ', i, '=', fib(i))

testFib(5)

print("\nPALINDROMES")
