print("################################################################################") 
print('''
EXCEPTIONS AS A CONTROL FLOW MECHANISM\n''')
print("################################################################################") 

print('''
Exceptions are not just purely for errors. They are a convenient flow control 
mechanism. In other programming languages, when something is gone a miss it is
normal to check whether something has been returned from every function
invocation, otherwise something similar to None should be returned. In Python,
it is more normal to have a function raise an exception when it cannot produce a
result that is consistent with the function's specification.
There is a syntax for this which causes a specified exception to be called and
is as follows:\n''')

print('''
raise exceptionName(arguments)\n''')

print('''
The exceptionName is usually one of the built-in exceptions. New exceptions can
be created by creating a new subclass. Most of the time the arguments to the
exception are a string which explains why the exception is being raised.\n''')
