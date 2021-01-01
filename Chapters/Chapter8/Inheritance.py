print("################################################################################") 
print('''
INHERITANCE\n''')
print("################################################################################") 

print('''
Inheritance provides a convenient mechanism to group related abstractions. 
It allows programmers to create a type hierarchy in which each type inherits
attribtues from the types above it in the hierarchy.
The class 'object' is at the top of the hierarchy. This makes sense, since in
Python everything that exists at run time is an object. Because Person inherits
all of the properties of objects, programs can bind a variable to a Person,
append a Person to a list, etc.
\n''')

import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

blockPrint()
from StudentsAndFaculty import Person
enablePrint()

print('''
class MITPerson(Person):
   
   nextIdNum = 0 #identification number

   def __init__(self, name):
       Person.__init__(self, name)
       self.idNum = MitPerson.nextIdNum
       MITPerson.nextIdNum += 1

   def getIdNum(self):
       return self.idNum

   def __lt__(self, other):
       return self.idNum < other.idNum
''')         

class MITPerson(Person):
    
    nextIdNum = 0 #identification number

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum


print('''
MITPerson is an example of a subclass of the Person class. It inherits the 
attributes of its superclass, in this case Person. The subclass can do
additional things:

    * Add new attributes, in this case the class variable nextIdNum, the
      instance variable idNum, and the method getIdNum
     
    * Ovverride, i.e., replace, attributes of the superclass. For example,
      MITPerson has overridden __init__ and __lt__. When a method has been
      overridden the version of the method that is executed is based on the object
      that is used to invoke the method. If the type of the object is the
      subclass, the version defined in the subclass will be used. If the type of
      the object is the superclass, the version in the superclass will be used.
      \n''')

print('''
The method MITPerson.__init__ first invokes Person.__init__ to intialize the
inherited instance variable self.name. It then initalizes self.idNum, an
instance variable that instances of MITPerson have but instances of Person do
not. 
The instance variable self.idNum is intialized using a class variable,
nextIdNum, that belongs to the class MITPerson, rather than to instances of the
class. When an instance of MITPerson is created, a new instance of nextIdNum is
not created. This allows __init__ to ensure that each instance of MITPerson has
a unique idNum. \n''')

print('''
Consider the following code:\n''')

print('''
p1 = MITPerson('Barbara Beaver')
print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))\n''')

print('''prints\n''')

p1 = MITPerson('Barbara Beaver')
print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))


print('''
The first line creates a new MITPerson. The second line is a bit more
complicated. When it attempts to evaluate the expression str(p1), the runtime
system first checks to see if there is an __str__ method associated with class
MITPerson. Since there is not, it next checks to see if there is an __str__
method associated with superclass, Person, of MITPerson. There is, so it uses
that. When the runtime system attempts to evaluate the expression p1.getidNum(),
it first checks to see if there is a get IdNum method associated with class
MITPerson. There is, so it invokes that method and prints the output
above.\n''')

print('''
Now consider the following:\n''')

print('''
p1 = MITPerson('MarkGuttag')
p2 = MITPerson('Billy Bob Beaver')
p3 = MITPerson('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')\n''')

p1 = MITPerson('MarkGuttag')
p2 = MITPerson('Billy Bob Beaver')
p3 = MITPerson('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')

print('''
We now have four virtual people, three of whom are named Bily Bob Beaver. Two of
the Billy Bobs are of type MITPeron and one merely a Person. If we execute the
lines of code:\n''')

print('''
print(' p1 < p2 =', p1 < p2)
print(' p3 < p2 =', p3 < p2)
print(' p4 < p2 =', p4 < p2)\n''')

print(' p1 < p2 =', p1 < p2)
print(' p3 < p2 =', p3 < p2)
print(' p4 < p2 =', p4 < p2)

print('''
Since p1, p2, and p3 are all of type MITPerson, the interpreter will use the 
__lt__ method defined in class MITPerson when evaluating the first two 
comparisons, so the ordering will be based on identification numbers. In the
third comparison, the < operator is applied to operand of different types.
Since the first argument of the expression is used to determine which __lt__
method to invoke, p4 < p1 is shorthand for p4.__lt__(p1). Therefore, the
interpreter uses the __lt__ method associated with the type of p4, Person, and
the "people" will be ordered by name.\n''')

print('''
What happens if we try\n''')

print('''
print('p1 < p4=', p1 < p4)\n''')
#print('p1 < p4=', p1 < p4)

print('''
We get an attribute error because the 'Person' instance has no attribute
'idNum' becuase the object to which p4 is bound does not have an attribute
idNum. \n''')
