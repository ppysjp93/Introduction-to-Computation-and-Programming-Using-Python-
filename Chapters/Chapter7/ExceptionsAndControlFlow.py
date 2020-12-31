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

print('''
Consider the following function definition:\n''')

print('''
def getRatios(vect1, vect2):
    """
    Assumes: vect1 and vect2 are equal length lists of numbers
    Returns: a list containing the meaningful values of vect1[i]/vect2[i]
    """
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios\n''')


def getRatios(vect1, vect2):
    """
    Assumes: vect1 and vect2 are equal length lists of numbers
    Returns: a list containing the meaningful values of vect1[i]/vect2[i]
    """
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios

print('''
It is quite clear how this these exceptions are working and how they are 
handling the different casese. \n''')

print('''
The following code demonstrates how getRatios might be used: \n''')

print('''
try: 
    print(getRatios([1.0,2.0,7.0,6.0], [1.0,2.0,0.0,3.0]))
    print(getRatios([], []))
    print(getRatios([1.0,2.0], [3.0]))
except ValueError as msg:
    print(msg)\n''')

try: 
    print(getRatios([1.0,2.0,7.0,6.0], [1.0,2.0,0.0,3.0]))
    print(getRatios([], []))
    print(getRatios([1.0,2.0], [3.0]))
except ValueError as msg:
    print(msg)

print('''
You can see that the argument for the ValuError has been assigned to the msg
variable.\n''')


print('''
def getRatios(vect1, vect2):
    """
    Assumes: vect1 and vect2 are equal length lists of numbers
    Returns: a list containing the meaningful values of vect1[i]/vect2[i]
    """
    ratios = []
    if len(vect1) != len(vect2):
        raise ValueError('getRatios called with bad arguments')
    for index in range(len(vect1)):
        vect1Elem = vect1[index]
        vect2Elem = vect2[index]
        if (type(vect1Elem) not in (int, float))\
            or (type(vect2Elem) not in (int, float))
            raise ValueError('getRatios called with bad arguments')
        if vect2Elem == 0.0:
            ratios.append(float('NaN')) #NaN = Not a Number
        else:
            ratios.append(vect1Elem/vect2Elem)
    return ratios\n''')


def getRatios(vect1, vect2):
    """
    Assumes: vect1 and vect2 are equal length lists of numbers
    Returns: a list containing the meaningful values of vect1[i]/vect2[i]
    """
    ratios = []
    if len(vect1) != len(vect2):
        raise ValueError('getRatios called with bad arguments')
    for index in range(len(vect1)):
        vect1Elem = vect1[index]
        vect2Elem = vect2[index]
        if (type(vect1Elem) not in (int, float))\
                or (type(vect2Elem) not in (int, float)):
            raise ValueError('getRatios called with bad arguments')
        if vect2Elem == 0.0:
            ratios.append(float('NaN')) #NaN = Not a Number
        else:
            ratios.append(vect1Elem/vect2Elem)
    return ratios

print('''
You can see that it is longer and more difficult to read, trying to implement
the same functioning code without using try and except statements.\n''')

print('''
Let's look at one final example.\n''')

print('''
def getGrades(fname):
    try:
        gradesFile = open(fname, 'r') #open file for reading
    except IOError:
        raise ValueError('getGrades could not open ' + fname)
    grades = []
    for line in gradesFile:
        try:
            grades.append(float(line))
        except:
            raise ValueError('Unable to convert line to float')
    return grades\n''')

def getGrades(fname):
    try:
        gradesFile = open(fname, 'r') #open file for reading
    except IOError:
        raise ValueError('getGrades could not open ' + fname)
    grades = []
    for line in gradesFile:
        try:
            grades.append(float(line))
        except:
            raise ValueError('Unable to convert line to float')
    return grades

print('''
try:
    grades = getGrades('quiz1grades.txt')
    grades.sort()
    median = grades[len(grades)//2]
    print('Median grade is', median)
except ValueError as errorMsg:
    print('Whoops.', errorMsg)\n''')

try:
    grades = getGrades('quiz1grades.txt')
    grades.sort()
    median = grades[len(grades)//2]
    print('Median grade is', median)
except ValueError as errorMsg:
    print('Whoops.', errorMsg)

print('''
Again we can see the use of try and except statements is of great use as a
method of flow control in our programs.\n''')
