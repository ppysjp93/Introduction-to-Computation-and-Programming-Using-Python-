print("################################################################################") 
print('''
MULTIPLE LEVELS OF INHERITANCE\n''')
print("################################################################################") 

from People import *

print('''
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year

class Grad(Student):
    pass
''')

print('''
Adding the class UG seems to make sense here because at least it has a body. 
However, why would we ever want to have the classes Student and Grad, since they
have no body.
By introducing the class Grad, we gain the ability to create two different kinds
of students and use their types to distinguish one kind of object form another.
For example:\n''')

print('''
p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)
print(p5, 'is a graduate student is', type(p5) == Grad)
print(p5, 'is an undergraduate student is', type(p5) == UG)''')

print('''
prints\n''')

p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)
print(p5, 'is a graduate student is', type(p5) == Grad)
print(p5, 'is an undergraduate student is', type(p5) == UG)

print('''
The utilitiy of the intermediate type Student is a bit subtler. Consider going
back to class MITPerson and adding the method\n''')

print('''
def isStudent(self):
    return isinstance(self, Student)\n''')

print('''
The function isinstance is built into Python. The first argument of isinstance
can be any object, but the second argument must be an object of type 'type'. The
function returns True if and only if the first argument is an instance of the
second argument. For example, the value of isinstance([1,2],list) is True.\n''')

print('''
Now consider the following example: \n''')

p3 = MITPerson('Billy Bob Beaver')

print(p5, 'is a student is', p5.isStudent())
print(p6, 'is a student is', p6.isStudent())
print(p3, 'is a student is', p3.isStudent())

print('''
Notice the meaning of isinstance (p6, Student) is quite differnt from the 
meaning of the type (p6) == Student. The object to which p6 is bound is of type
UG, not student, but since UG is a sbclass of Student, teh object to which p6 is
bound is considered to be an instance of class Student (as well as an instance
of MITPerson and Person).
Since there are only two kinds of students, we could have implemented isStudent
as,\n''')

print('''
def isStudent(self):
    return type(self) == Grad or type(self) == UG\n''')

def isStudent(self):
    return type(self) == Grad or type(self) == UG

print('''
However, if a new type of student were introduced at some later point it would
be necessary to go back and edit the code implementing isStudent. By introducing
the intermediate class Student and using is instance we aoid this porblem. For
example, if we were to add\n''')

print('''
class TransferStudent(Student):
    def __init__(self, name, fromSchool):
        MITPerson.__init__(self, name)
        self.fromSchool = fromSchool

    def getOldSchool(self):
        return self.fromSchool
''')

print('''
no change needs to be made to isStudent. 
It is not unusual during hte creation and later maintenance of a program to go
back and add new classes or new attributes to old classes. Good programmers
design their programs so as to minimize the amount of code that might need to be
changed when that is done.\n''')
