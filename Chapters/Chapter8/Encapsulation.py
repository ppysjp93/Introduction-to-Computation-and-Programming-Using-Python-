print("################################################################################") 
print('''
ENCAPSULATION AND INFORMATION HIDING\n''')
print("################################################################################") 

from Grades import *
from People import *

print('''
We are going to create a class called 'Grades' that can keep track of grades 
for a collection of students. To do this, we design Grades so that it uses two
data structures the dictionary and the list. The dictionary maps a student's
identification number to a list of grades. The list keeps track of the students
in the class. 
There are two functions key functions we create for Students. getGrades, which
returns a copy of the list of grades assoicated with a student, and getStudents
returns a copy of the list of students. The computational cost of copying the
lists could have been avoided by simply returning the instance variables
themselves. doing so, however, is likely to lead to problems.
Coinsider the following:

    allStudents = course.getStudents()

    allStudents.extend(course2.getStudents())
If getStudents returned self.students, the second line of code would have hte
(probably unexpected) side effect of chanign the set of students in course1.
The instance variable isSorted is sued to keep track of whether or not the list
of students has been sorted since the last time a student was added to it. This
allows the implementaiton of getStudents to avoid sorting a nalready sorted
list.\n''')

print('''
We now define a function that uses the class Grades to produce a rade report 
for some students taking a course named sixHundred.\n''')


print('''
def gradeReport(course):
    """
    Assumes course is of type Grades
    """
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report = report + '\\n'
                     + str(s) +''s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\\n'\ + str(s) + 'has no grades' 
    return report
''')

def gradeReport(course):
    """
    Assumes course is of type Grades
    """
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report = report + '\n'\
                     + str(s) +'\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n'\
                     + str(s) +'has no grades' 
    return report

print('''
ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')
sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)
for s in sixHundred.getStudents():
    sixHundred.addGrade(s, 75)
sixHundred.addGrade(g1, 25)
sixHundred.addGrade(g2, 100)
sixHundred.addStudent(ug3)
print(gradeReport(sixHundred))
''')

ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')
sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)
for s in sixHundred.getStudents():
    sixHundred.addGrade(s, 75)
sixHundred.addGrade(g1, 25)
sixHundred.addGrade(g2, 100)
sixHundred.addStudent(ug3)
print(gradeReport(sixHundred))


print('''
There are two important concepts at the heart of object-oriented programming. 
The first is the idea of encapsulation. By this we mean the bundling together of
data attributes and the methods for operating on them. For example, if we write
Rafael = MITPerson('Rafael Reif')
we can use dot notation to access attributes such as Rafael's name and
identification number. The second important concept is information hiding. This
is one of the keys to modularity. If those parts of the program that use a class
(i.e., the clients of the class) rely only on the specification of the methods
in the class, a programmer implementing the class is free to change the
implementation of the class (e.g., to improve efficiency) without worry that the
change will break the code that uses the teh class.
Some programming languages (Java and C++ for example) provide mechanisms for
enforcing information hiding. Programmers can make the attributes of a class
'private', so that clients of the class can access the data only through the
object's methods. Python 3 uses a naming convention to make attributes invisible
outside the class. When the name of an attribute starts with __ but does not end
with __, that attribute is not visisble outside the class. 
Consider the following class:\n''')

print('''
class infoHiding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsoVisible__ = 'Look at me too'
        self.__invisible = 'Dont\'t look at me directly'

    def printVisisble(self):
        print(self.visisble)

    def printInvisible(self):
        print(self.__invisisble)

    def __printInvisible(self):
        print(self.__invisible)

    def __printInvisible__(self):
        print(self.__invisible)
''')

class infoHiding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsoVisible__ = 'Look at me too'
        self.__invisible = 'Dont\'t look at me directly'

    def printVisisble(self):
        print(self.visisble)

    def printInvisible(self):
        print(self.__invisible)

    def __printInvisible(self):
        print(self.__invisible)

    def __printInvisible__(self):
        print(self.__invisible)

print('''
When we run the code\n''')

print('''
test = infoHiding()
print(test.visible)
print(test.__alsoVisible__)
print(test.__invisible)\n # We get an attribute error from this one''')

print('''
it prints\n''')

test = infoHiding()
print(test.visible)
print(test.__alsoVisible__)
#print(test.__invisible)

print('''
The code:\n''')

print('''
test = inforHiding()
test.printInvisible()
test.__printInvisible__()
test.__printInvisible() # We get an Error: 'infoHiding' object has no attribute
'__printInvisisble'
''')

print('''
prints\n''')

test = infoHiding()
test.printInvisible()
test.__printInvisible__()
#test.__printInvisible()

print('''
And the code:\n''')

print('''
class subClass(infoHiding):
    def newPrintInvisible(self):
        print(self.__invisible)

testSub = subClass()
testSub.newPrintInvisible() # AttributeError: 'subClass' object has no attribute
'_subClass__invisible'
''')

class subClass(infoHiding):
    def newPrintInvisible(self):
        print(self.__invisible)

testSub = subClass()
#testSub.newPrintInvisible()

print('''
It is important to note that when a subclass attempts to use a hidden attribute
of its supeclass an AttributeError occurs. This makes information hiding in
Python a bit cumbersome.
Because it can be cumbersome, many Python programmers do not take advantage of
the __ mechanism for hiding attribtues -- as we don't in this book. So for
example a client of Person can write the expression Rafael.lastName rather tahn
Rafael.getLastname().
This is unfortuante because it allows the client code to rely upon something
that is not part of the speciication of Person, and is therefore subject to
change. If the implementaiton of Person were changed, for example to extract the
last name whenever it is requested rather than store it in an instance variable,
then the client code would no longer work. 
Not only does Python let programs read instance and class variables from outside
the class defintion, it also lets programs write these variables. So, for
example, the code Rafael.birthday = '8/21/50' is perfectly legal. This would
lead to a runtime type errror, were Rafael.getAge invoked later in teh
computation. It is even possible to create instance variables from outside the
class definition. For example, Python will not complain if the assingment
statement:
me.age = Rafael.getIdNum()
occurs outside the class definition. 
While this relatively weak static sematic checking is a flaw in Python, it is
not a fatal flaw, A disciplined programmer can simly follw the sensible rule of
not directly accessing data attributes from outside the class in which they are
defined as we do in this book.\n''')
