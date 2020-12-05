print("################################################################################") 
print("""
INTRO TO PYTHON""")
print("################################################################################") 
 
print("""
There are different programming languages which have different properties
* Low Level vs High Level
    Move 64 bits of data from this location to that location.
* General versus Targeted to an Application Domain
    SQL is great for Databases but terrible for creating an operating system
* Interpreted versus Compiled
    Interpreted languages are much easier to debug because the interpreter can
    produce error messages. Compiled lanuages usually produce programs that run
    more quickly and use less space.""")

print("""
The goal of this book is to teach the reader how to write programs that solve 
problems (as well as python). Python is a great programming language that can be 
used to pretty much make anything that doesn't require direct access to the 
computers hardware. Python is not great fro programs that require high 
high reliability constraints because of its weak static semantic checking.""")

print("""
(What is static semantic checking?)
A statically typed language is one in which each declared variable's types is 
declared at compile time which is before when the program runs. It illiminates 
a group of bugs which are created as a result of "grammatical" errors in the code. 
Imagine you attempted to do the operation '5' * '6'. This kind of error will be 
found whilst you are programming not during the running of the program. """)

print("""
Though python isn't statically typed it is particularly useful as it is relatively 
simple syntactically and it has a large number of libraries that interface with 
Python which extend its functionailty.""")

print("\nBASIC ELEMENTS OF PYTHON")

print('Yankees rule!')
print('But not in Boston!')
print('Yankees rule,', 'but not in Boston!')

print("\nOBJECTS, EXPRESSIONS AND NUMERICAL TYPES")

print("""
The next bit is really good. It says to think of Types as either scalar or 
non-scalar. As in scalar types are atomic i.e. indivisible whilst non-scalar
object like string do have an internal structure.
Python in particular has 4 sclar objects: int, float, bool and None""")

print("""
The book goes on to explain basic programming arithmetic which I know.""")

print("\nVARIABLES AND ASSIGNMENT")

print("""
In python it is critical to remember that a variable is just a name and nothing
more. An assignment statement associates the left of the = symbol with the object 
denoted by the expression to the right fo the =.""")

print("""
Variables cannot start with numbers. There is also a list of reserved words which
have a special meaning so they cannot be used as names for variables, the list 
is as follows:
    and, as, assert,, break, class, continue, def, del, elif, else, except, False,
    finally, for, from, global, if, import, in, is, lambda, nonlocal, None, not,
    or, pass, raise, return, True, try, while, with, yield""")

print("""
Using comments is a good way to improve readability (this is for programms you 
will be making yourself. Comments should be used sparingly in commercial 
enviroments because the code itself should be descriptive enough.) Below is an 
example of commenting anyways: """)

side = 1 # length of sides of a unit square
radius = 1 # radius of a unit circle
pi = 3.14
# subtract area of unit circule from area of unit square
areaC = pi*radius**2
areaS = side*side
difference = areaS - areaC

print("""
Python allows multiple assigments to be performed. 
x, y = 2, 3 will bind x to 2 and y to 3 """)

print("""
It then goes on to explain using an IDE rather than typing code directly into 
the shell (which is what I like to do most because vim) """)
