print("################################################################################") 
print('''
MULTIPLE LEVELS OF INHERITANCE\n''')
print("################################################################################") 

import People

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

print('''
Adding the class UG seems to make sense here because at least it has a body. 
However, why would we ever want to have the classes Student and Grad, since they
have no body.
By introducing the class Grad, we gain the ability to create two different kinds
of students and sue their types to distinguish one kind of object form another.
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
can be any object, but the second argument must be an object of type type. The
function returns True if and only if the first argument is an instance of the
second argument. For example, the value of isinstance([1,2],list) is True.\n''')

print('''
Now consider the following example: \n''')



print(p5, 'is a student is', p5.isStudent())
print(p6, 'is a student is', p6.isStudent())
print(p3, 'is a student is', p3.isStudent())
