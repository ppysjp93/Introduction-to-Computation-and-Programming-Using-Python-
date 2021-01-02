print("################################################################################") 
print('''
GENERATORS\n''')
print("################################################################################") 

from Grades import *
from People import *

print('''
A perceived risk of information hiding is that preventing client programs from 
directly accessing critical data structures leads to an unacceptable loss of
effiency. In the early days of data abstraction, many were concerned about the
cost of introducing extraneous function/method calls. Modern comilation
technology makes this concern moot. A more serious issue is that client programs
will be forced to use inefficient algorithms.
Consider the implementation of gradeReport function (see Encapsulation.py). The
invocation of course.getStudents creates and returns a list of size n, where n
is the number of students. This is probably not a problem for a grade boo for a
single class, but imagine keeping tack of the grades of 1.7 million high school
students taking the SATs. Creating a new list of tha size when the list already
exists is a significant inefficiency. One solution is to abandon the abstraction
anad allow gradeReport to directly access the instance variable course.students,
but that would violate information hiding. Fortunately, there is a better
solution. \n''')

print('''
def getStudents(self):
    """Return a sorted list of the students in the grade book"""
    if not self.isSorted:
        self.students.sort()
        self.isSorted = True
    return self.students[:]\n''')

print('''
This code becomes very inefficent when we consider millions of students. The
following uses the yield key word and is an example of a generator which is much
more efficient as it doesn't mean that the entire students list needs to be 
regenerated when it is called:\n''')

print('''
def getStudents(self):
    """
    Return the studetns in the grade book one at a time in alphabetical order
    """
    if not self.isSorted:
        self.students.sort()
        self.isSorted = True
    for s in self.students:
        yield s
''')

def getStudents(self):
    """
    Return the studetns in the grade book one at a time in alphabetical order
    """
    if not self.isSorted:
        self.students.sort()
        self.isSorted = True
    for s in self.students:
        yield s

print('''
Any function that contains a yield statement is treated in a special way.
'yield' tells Python that the function is a generator. Genrators are typically
used in conjunction with for statements, as in 

for s in course.getStudents():\n''')

print('''
At the start of the first iteration of a for loop that uses a generator, the
generator is invoked and runs until the first time a yield statement is
executed, at which point it returns a value of the expression in the yield
statement. On the next iteration, the generator resumes execution immediately
following the yield, with all local variables bound to the objects to which they
were bound when the yield statement was executed, and again runs until a yield
statement is executed. It continues to do this until it runs out of code to
execute or executes a return statement, at which point the loop is exited.
This allows programmers to use a for loop to iterate over the students in objects
of type Grades in the same way they can use a for loop to iterate over the
elements of built-in types such as list. For example:\n''')

print('''
book = Grades()
book.addStudent(Grad('Julie'))
book.addStudent(Grad('Charlie'))
for s in book.getStudents():
    print(s)
''')

book = GradesWithGenerator()
book.addStudent(Grad('Julie'))
book.addStudent(Grad('Charlie'))
for s in book.getStudents():
    print(s)

print('''
The the for loop on line 107 of Encapsulation.py wouldn't need to be refactored 
if we chose to use the new definition for the getStudents method (however all
the code relying on the fact that getStudents returned a list would.) The same
loop can iterate over the values provided by getStdents regardless of whetehr
getStudents returns a list of values or genrates one value at a time. Generating
one vlaue at a time will be more efficient, because a new list containing the
students will not be created.\n''')
