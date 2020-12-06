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
with lists, as showin Figure 5.5.""")

def applyToEach(L,f):
    """
    Assumes L is  a list, f a function
    Mutates L by replacing each element, e, of L by f(e)
    """
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1, -2, 3.33]
print('L =', L)
print('Apply abs to each element of L.')
applyToEach(L, abs)
print('L =', L)
print('Apply int to each element of L.')
applyToEach(L, int)
print('L =', L)
print('Apply factorial to each element of L.')
applyToEach(L, factR)
print('L =', L)
print('Apply Fibonacci to each element of L.')
applyToEach(L, fib)

