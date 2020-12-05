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

print("""
Below is the function isPalindrome, it contains two helper functions. These are
of no interest to the client but are a useful way of breaking up a problem into
parts. The helper function toChars conerts all letters to lowercase and removes
non-letters. It starts by using a built-in method oon strings to generate a
string that is idenctical to s except that all uppercase letters have been
converted to lowercase. This is an example of method invocation which will be
discussed further when we get to classes. 
The next helper function isPal does the real work. The two base cases are
strings of length zero or one. This means that the recursive part of the
implementation is reached only on strings of length two or more. The conjunction
in the else clause is evaluated from left to right. The code first checks
whether the first and last characters are the same, and if they are goes on to
check whether the string minus those two characters is a palindrome. That the
second conjunct is not evaulated unless the first conjunct evaluates to True is
semantically irrelevant in this example. However, later in the book we will see
examples where this kind of short-circuit evauluation of Booelan expressiosn is
semantically relevant. """)

def isPalindrom(s):
    """Assumes s is a str
       Retruns True if letters in s form a palindrom; False
       otherwise. Non-letters and capitalization are ignored."""

    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))
            
print("""
This is a really nice example of how slicing is used in a string data structure
recursively. I think that is the key, is the input to the recursive function 
should just be a smaller version of the same problem.""")

print("\nIs racecar a Palindrome? ")
racecar = isPalindrome('Racecar')


print("""
isPalindrome is an example of using the divide and conquer method to find a
solution to a problem. To solve the problem you break the original version of
the problem into a simpler version of the same problem. In this case checking
whether a shorter string is a Palindrome and and thing we know how to do which
is compare two single characters. We then combine the solutions with the and
keyword.

Interesting fact when two Boolean-valued expressions are oconnected by "and",
each expression is called a conjunct. If they are connected by "or" they are
called disjuncts.""")
