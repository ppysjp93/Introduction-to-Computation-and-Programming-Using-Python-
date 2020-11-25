print("################################################################################") 
print("""
SCOPING""")
print("################################################################################") 

print("""
Consider the following example: """)

print("""
    def f(x):
        y = 1
        x = x + y
        print('x =', x)
        return x""")

def f(x):
    y = 1
    x = x + y
    print('x =', x)
    return x

print("""
x = 3 
y = 2
z = f(x) # value of x used as actual parameter
print('x =', x)
print('y =', y)
print('z =', z)""")


x = 3 
y = 2
z = f(x) # value of x used as actual parameter
print('x =', x)
print('y =', y)
print('z =', z)

print("""
Remember the function f(x) has a print statement in it! At the function call of
f the formal parameter x is bound to the actual parameter x. It is very
important to note that even though the actual and formal parameters have the
same name, they are not the same variable. The formal parameter x and the 'local
variable' y that are used in f exist only within the scrope of the definition of
f The assignment statement x = x + y within the funciton body binds the local
name x t othe object 4. The assignments in f have no effect at all on the
bindings of the names x and y that exist outside the scope of f. """)

print("""
Another way to think of this would be:
    * At the top level, the level of the shell, a 'symbol table' keeps track of
        all names defined at that level and their current bindings.
    * When a function is called a new symbol table (often called a 'stack
        frame') is created. This table keeps track of all names defined within the
        function (including the formal parameters) and their current bindings. If a
        function is called from within the function body, yet another stack frame is
        created.  
    * When the function completes, its stack frame goes away.""")

print("""
Python is lexically scoped, which means you can determine the scope of a name by
looking at the text. """)

print("""
def f(x):
    def g():
        x = 'abc'
        print('x =', x)
    def h():
        z = x
        print('z = ', z)
    x = x + 1
    print('x =', x)
    h()
    g()
    print('x = ', x)
    return g""")

def f(x):
    def g():
        x = 'abc'
        print('x =', x)
    def h():
        z = x
        print('z = ', z)
    x = x + 1
    print('x =', x)
    h()
    g()
    print('x = ', x)
    return g

print("""
x = 3
z = f(x)
print('x =', x)
print('z =', z)
z()\n""")

x = 3
z = f(x)
print('x =', x)
print('z =', z)
z()


print("""
We open with the global stack frame, which has the variables x and z and the
function name f. The assignment statement z = f(x) first evaluates f(x) this 
creates a stackframe where the x in the scope of f(x) is initially assigned 
to point at what x is pointing at in the global frame (3 in the case). Then 2 
more functions are defined within f(x) (h() and g()). The next thing that 
happens is the variable x is incremented by 1 in the scope of f(x) so that 
the value of x is now 4. Next h() is called. This introduces another stack frame
Something weird happens here because in this function  we have a variable z being 
assigned to the 'variable' x eventhough x hasn't been previuosly assigned a 
'value'. This is where we start to get to a fundamental understanding of Python.
What python does in this case is it looks through the current stack frame and
sees if there is a variable x which has been assigned a value. It then will set
the variable to the value further down the stack frame if it exists otherwise
there will be an error with the Python interpreter. So, having looked through
the stack frame z now points at the value 4, and the print statement inside the
stack frame for h is executed and the stack frame for h is popped off the top of
the stack. Next a new stack frame is added for the function of g(). In this case
the local variable x is printed with the assigned local value 'abc' and the 
stack frame associated with g() is popped from the stack. Back in the scope of f
the local variable x still points at the value for x which was incremented
earlier to be 4, so that value is then printed. Now the stack frame for f is
popped off the stack and z is assigned to g, ( z = g ) Next, the value of x is
printed for the local value of x which is 3 (global value of x is 3). Now
another bit of Python understanding comes in here, z = g, and so is just a
function, it has no value which is why we get the strange output. It also
explains the next bit of code because z() means we are doing g() and we know the
output of g() is " x = 'abc' " """)


