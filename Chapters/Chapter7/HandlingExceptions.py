print("################################################################################") 
print("""
HANDLING EXCEPTIONS\n""")
print("################################################################################") 

print("""
Up to now, we have treated exceptions as fatal events. An unhandled exception is
one that causes the program to terminate. There are many occasions where an
exception is something that the programmer is anticipating and so should be
handled. A user may enter something that is inappropriate for example.
If you know that a line of code is going to cause an exception then you should
make the effort to handle the exception. Consider the following: \n""")

print("""
successFailureRatio = numSuccesses/numFailures
print('The success/failure ratio is', successFailureRatio)
print('Now here')\n""")

print("""
Most of the time this code will work. But it will fail if numFailures happens to
be zero. If it is zero it will raise a ZeroDivisionError exception and the print
statements will never be reached.\n""")

print("""
A better version of the code would be the following:\n""")

print("""
try:
    successFailureRatio = numSuccesses/numFailures
    print('The success/failure ratio is', successFailureRatio)
except ZeroDivisionError:
    print('No failures, so th esuccess/failure ratio is undefined.')
print('Now here')\n""")

print("""
If there is no ZeroDivionError, then the try block is executed in its entirity,
the except block is skipped and then the final print statment is executed.
If we encounter a ZeroDivision error, the rest of the try block is skipped 
immediately, the except block is excecuted in its entirety and then the final
print statment is executed. \n""")

print("""
Consider the following example:\n""")

print("""
val = int(input('Enter an integer: '))
print('The square of the number you entered is', val**2)\n""")

print("""
If the user obligingly types a string that can be converted to an integer,
eveything will be fine. But if a user enters a string with any characters that
aren't numbers (a simple case would be "abc", then we get a ValueError exception
and the print statement will never be reached. The following is what the
programmer should have written.\n""")

print("""
while True:
    val = input('Enter an integer: ')
    try:
        val = int(val)
        print('The square of the number you entered is', val**2)
        break #to exit the while loop
    except ValueError:
        print(val, 'is not an integer')\n""")

print("""
This functionality can be generalised to a function and we can then also
generalise this further and create a function that tests for any type of
input.\n""")
  

print("""
def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg + ' ')
        try:
            return (valType(val)) # convert str to valType before returning
        except ValueError:
            print(val, errorMsg)\n""")

print("""
readVal(int, 'Enter an integer:', 'is not an integer')\n""")

def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg + ' ')
        try:
            return (valType(val)) # convert str to valType before returning
        except ValueError:
            print(val, errorMsg)

print("""
The function readVal is polymorphic, i.e., it works for arguments of many
different types. Such functions are easy to write in Python, since types are
first-class objects. We can now ask for an integer using the code\n""")

print("""
val = readVal(int, 'Enter an integer:', 'is not an integer')\n""")

print("""
There are 2 other alternatives to exceptions mentioned in this paragraph. One
would be to cause a string to return its bits used to encode the string. This
however is unlikely to have anything to do with the program being created. The
other alternative is to return the special value None. However code would still
be required to handle whether the function had returned None. If this wasn't
checked there may be some strange error that could occur.\n""")

print('''
The fact that the program throws an exception is a good thing because overt bugs
are way better than covert bugs.\n''')

print('''
Finally, it is possible for a block of code to throw more than one type of
exception, the following syntax is how this would be done: \n''')

print('''
except (ValueError, TypeError):\n''')

print('''
Alternatively we can write an except block for each kind of xception which will
then allow the program to chose an action based upon which exception was
raised.\n''')

print('''
except: \n''')

print('''
This statement by itself will catch any exception that is raied within a try
block.\n''')

