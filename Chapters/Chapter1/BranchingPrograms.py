print("################################################################################") 
print("""
BRANCHING PROGRAMS""")
print("################################################################################") 
 
print("""
Linear programs are pretty boring as they just execute one statement one after 
the other whereas programs like that branch are able to execute code in varying 
orders. Branching is done using a conditional statement. The is then a nice 
diagram explaing how the true or false block will be then executed depending on
the conditional. 
The structure of a conditional in python is as follows:
    if Boolean expression:
        block of code
    else:
        block of code
or 
    if Boolean expression:
        block of code""")

print("\nEXAMPLE 1")

print("""
if x%2 == 0 
    print('Even')
else:
    print('Odd')
    print('Done with conditional')
In this case we set x to be 1\n""")

x = 1

if x%2 == 0: 
    print('Even')
else:
    print('Odd')
print('Done with conditional')


print("""
Indentation has meaning in python, this is very important to remember!
You can also indenct conditions like as follows.""") 

print("\nEXAMPLE 2")

print("""
if x%2 == 0: 
    if x % 3:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 adnd not by 3')
    elif x % 3 == 0: 
        print('Divisible by 3 and not by 2')""")


x = 117
print("\nx = \n", str(x))

if x%2 == 0: 
    if x % 3:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 adnd not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')


print("""
You can also compound expressions""")

print("\nEXAMPLE 3 ")

print("""
if x < y and x < z: 
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')""")


x = 2 
y = 3 
z = 4

print("\nx = \n", str(x))
print("\ny = \n", str(y))
print("\nz = \n", str(z))

if x < y and x < z: 
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')

print("\nINTERESTING POINT AND NEW WAY OF THINKING")

print("""
Conditions give us a way of writing programs that are not straight-lined.
If a line of code takes one unit of time to execute and a straightline program
has n lines of code, it will take n units of time to run. But branching programs
with n lines of code? They may take less than n units of time to run but they 
can't take mroe, since each line of code is executed more than once. A program
whose bounded by the length of the program is said to run in constant time. 
This does not mean that each time it is run it executes the same number of steps.
It means that there exists a constant, k, such that the program is guaranteed to 
no more than k steps to run. Constant time programs are quite limited in what 
they can do.""")
