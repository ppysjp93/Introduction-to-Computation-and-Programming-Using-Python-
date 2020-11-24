print("################################################################################") 
print("""
FUNCTIONS AND SCOPING""")
print("################################################################################") 

print("""
Here is an example of a function. You are already pretty comfortable with these
but its worth going over some of the semantics. """)

def maxVal(x, y):
    if x > y:
        return x
    else: 
        return y
    
print("""
def is a reserved word that tell Python that a function is about to be defined.
The function nmae (maxVal in this example) is simply a name that is sued to
refer to the function. The sequence of names within the parentheses follwing the
function name (x, y in this example) are 'formal parameters' of the function.
When the function is sued, the formal parameters are bound to the actual
parameters (often referred to as arguments) of the function invocation (also
referred to teh as a function call). For example, the invocation
maxval(3, 4)\n""")

print("\nmaxVal = ", str(maxVal(3, 4)))

print("""
During the invocation x binds to 3 and y binds to 4""")

print("""
'return' is a special statement in Python that can only be used within a
function. Consider the following product = maxVal(3,4)*maxVal(3,2)""")

print("\nproduct = ", str(maxVal(3,4)*maxVal(3,2)))

print("""
It's clear that 4 was returned from the first function invocation and 3 was
returned from the second function invocation. These value were then multiplied
together to get 12.""")


print("""
The 'point of execution' is the next instruction to be executed after the 'point
of invocation' to the first statement in the body of the function. The code of
the function is then executed until either a retrun statement is encountered, in
which case whatever is follwoing the return statement becomes the value of the
function invocation or there are no more statement to execute in which case the
value 'None' is returned. If no expression follows the return statement the
value of the invocation is None. The 'value of the invocation' is the returned
value. The 'point of exectuion is transferred back to the code immediately
follwing the invocation. Basically the 'point of execution' is like an arrow
that points at a line of code. By creating a function the arrow no longer jumps
around one line after the next, it will jump inside a function and go through
line by line and then jump again, so we start to get a more complex movement of
this pointer.""")

print("""
Parameters provide something call 'lambda abstraction', allowing programmers to
write code that manipulates not specific objects, but instead whatever objects
the called of hte function chooses to use as actual parameters. A 'lambda
abstraction' is like a non-'type'racist abstraction. """)



