import Chapters.Chapter4.Recursion as Rec

print("################################################################################") 
print("""
FUNCTIONS AS OBJECTS\n""")
print("################################################################################") 

print("""
In python, functions are 'first class objects'. This means that they can be 
treated like objects of any other type, eg., int or list. They have types, eg.,
the expression type(abs) has the value <type 'built-in_function_or_method'>;
they can appear in expressions, e.e., as the right-hand side of an asignemnt
statement or as an arguemtn to a function; they can be elements of lists; etc.
Using functions as arguements allows a style of coding called
'higher-order programming'. It can be particularly convenient in conjunction
with lists, as showin Figure 5.5\n""")

print('''
def applyToEach(L,f):
    """
    Assumes L is  a list, f a function
    Mutates L by replacing each element, e, of L by f(e)
    """
    for i in range(len(L)):
        L[i] = f(L[i])\n''')

def applyToEach(L,f):
    """
    Assumes L is  a list, f a function
    Mutates L by replacing each element, e, of L by f(e)
    """
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1, -2, 3.33]
print('L =', L)
print('\nApply abs to each element of L.')
applyToEach(L, abs)
print('L =', L)
print('\nApply int to each element of L.')
applyToEach(L, int)
print('L =', L)
print('\nApply factorial to each element of L.')
applyToEach(L, Rec.factR)
print('L =', L)
print('\nApply Fibonacci to each element of L.')
applyToEach(L,Rec.fib)
print('L =', L)

print("""
applyToEach is called 'higher-order' because it has an argument that is itself a
function. The first time it is called, it mutates L by applying the unary
built-in function abs to each element. The second time it is called, it applies
a type conversion to each element. The thrid time it is called, it replaces each
lement by the result of applying the function factR. And the fourth time it is
called, it replaces each element by the result of applying the function fib to
element.""")

print("""Python has a built-in higher-order function, map that is similar to, but more
general than, the applyToEach function defined above, it is designed to be used
in conjunction with a for loop. In its simples form the first argument to map is
a unary function (i.e., a function that has only one parameter) and the second
argument is any ordered collection of values suitable as arguments to the first
argument.
When used in a for loop, map behaves like range function in that it returns one
value for each iteration of the loop. These values are generated by applying the
first argument ot each element of the second arguemtn. For example, the code

for i in map(fib, [2, 6, 4])
    print(i)

prints\n""")

for i in map(Rec.fib, [2, 6, 4]):
    print(i)

print("""
More generally, the first argument to map can be a function of n arguments, in
which case it must be follwoed by n subsequent ordered collections (each of the
same length). For example, the code 

L1 = [1, 28, 36]
L2 = [2, 57, 9]

for i in map(min, L1, L2): 
    print(i)""")

L1 = [1, 28, 36]
L2 = [2, 57, 9]

for i in map(min, L1, L2): 
    print(i)

print("""
Python supports the creation of a anonymous functions (i.e., functions that are
not bound to a name), using the reserved word lambda. The general form of lambda
expressions is
    lambda <sequence of variablenames>: <expression>
For example, the lambda expression lambda x, y: x*y retruns a function that
returns the product of it two arguments. Lambda expressions are frequently used
as arguments to 'higher-order' functions. For example:""")


print("""
L = [] 
for i in map(lambda x, y: x**y, [1, 2, 3, 4], [3, 2, 1, 0]):
    L.append(i)
print(L)\n""")

L = [] 
for i in map(lambda x, y: x**y, [1, 2, 3, 4], [3, 2, 1, 0]):
    L.append(i)
print(L)
