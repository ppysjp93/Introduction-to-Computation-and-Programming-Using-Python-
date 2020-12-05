print("################################################################################") 
print("""
KEYWORD ARGUMENTS AND DEFAULT VALUES""")
print("################################################################################") 

print("""
In python, there are two ways that formal parameters get bound to actual
parameters. The most common method is 'positional', the first formal parameter
is bound to the first actual parameter, the second formal to teh second actual
and so on. Python also supports keyword arguments, in which formals are bound to
actuals using the name of hte formal parameter. 
See below:
    def printName(firstName, lastName, reverse):
        if reverse:
            print(lastName + ', ' + firstName)
        else:
            print(firstName, lastName)""")

print("""
printName('Olga', 'Puchmajerova', False)
printName('Olga', 'Puchmajerova', reverse = False)
printName('Olga', lastName = 'Puchmajerova', False)
printName(lastName = 'Puchmajerova', 'Olga', reverse = False)""")

def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)

printName('Olga', 'Puchmajerova', False)
printName('Olga', 'Puchmajerova', reverse = False)
printName('Olga', lastName = 'Puchmajerova', reverse = False)
printName(lastName = 'Puchmajerova', firstName ='Olga', reverse = False)

print("""
Keyword arguents must follow positional arguments in python. The following will
produce an error: 
    printName(lastName = 'Puchmajerova',lastName = 'Olga',  False)""")

print("""
Keyword Arguments are often used in tandem with default parameter values:""")

def printName(firstName, lastName, reverse = False):

    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)

print("""
Default values allow the programmer to call the function with fewer parameters: 
For example:""")

print("""
printName('Olga', 'Puchmajerova')
printName('Olga', 'Puchmajerova' True)
printName('Olga', 'Puchmajerova' reverse = True)""")

print("""
prints...\n""")

printName('Olga', 'Puchmajerova')
printName('Olga', 'Puchmajerova', True)
printName('Olga', 'Puchmajerova', reverse = True)

print("""
The last of these gives some documentation for the perhaps mysterious argument 
true. So be kind to your future self and use kwargs if a formal parameter binds
to a variable miles from the function definition.""")



