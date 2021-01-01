print("################################################################################") 
print('''
USING CLASSES TO KEEP TRACK OF STUDENTS AND FACULTY\n''')
print("################################################################################") 

print('''
Consider the case where you are designing a program that keeps track of all the
students and faculty at a university. It is possible to do this without data
abrstraction by using a combination of lists and dictonaries. Keeping track fo
faculty and staff would also require some similar data structures and some
different data structures, data structures to keep track of things like salary
history for example.
Before rushing in to design a bunch of data structures, let's think about some
abstractions that might prove useful. Is there an abstraction that covers the
common attributes of students, professors, and staff? Some would argue that they
are all human. The following code is a class that incorporates some of the
common attribtues of humans. It makes use of the standard Python library module
datetime, which proivdes many convenient methods for creating and manipulating
data.\n''')

import datetime

print('''
class Person(object):

    def __init__(self, name):
        """
        Creat a person
        """
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
        
    def getName(self):
        """
        Returns self's full name
        """
        return self.name

    def getLastName(self):
        """
        Returns selfs last name
        """
        return self.lastName

    def setBirthday(self,birthdate):
        """
        Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate
        """
        self.birthday = birthdate

    def getAge(self):
        """
        Returns self's current age in days
        """
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """
        Returns True if self precedes other in alphabetical order, and False
        otherwise. Comparison is based on last names., but if these are the same
        full names are compared.
        """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """
        Returns self's name
        """
        return self.name

me = Person('Micheal Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')
print(him.getLastName())
him.setBirthday(datetime.date(1961, 8, 4))
her.setBirthday(datetime.date(1958, 8, 16))
print(him.getName(), 'is', him.getAge(), 'days old')
''')

class Person(object):

    def __init__(self, name):
        """
        Creat a person
        """
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
        
    def getName(self):
        """
        Returns self's full name
        """
        return self.name

    def getLastName(self):
        """
        Returns selfs last name
        """
        return self.lastName

    def setBirthday(self,birthdate):
        """
        Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate
        """
        self.birthday = birthdate

    def getAge(self):
        """
        Returns self's current age in days
        """
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """
        Returns True if self precedes other in alphabetical order, and False
        otherwise. Comparison is based on last names., but if these are the same
        full names are compared.
        """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """
        Returns self's name
        """
        return self.name

me = Person('Micheal Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')
print(him.getLastName())
him.setBirthday(datetime.date(1961, 8, 4))
her.setBirthday(datetime.date(1958, 8, 16))
print(him.getName(), 'is', him.getAge(), 'days old')

print('''
Notice that to instanciate a person an agument must be supplied to the __init__
function. It generally considered poor form to directly access the information
about these instances and is much better to use a 'getter'. In addition, this
implementation has no way for the user to get the Birthday despite there is an
attribute to set that value. (This can be easily fixed with a getBirthday()
method).  \n''')

print('''
This class also implements another special method __lt__. This method overloads
the < operator. The __lt__ method will get called if the first agument to the <
operator is of type Person. The __lt__ method in class Person is implemnted usin
the binary < operator of type str. The expression self.name < other.name is
shorhand for self.name.__lt__(other.name). Since self.name is of type str, this
__lt__ method is the one associated with type str. 
Another benefit to overloading the < operater, is that it provides automatic
access to any polymorphic method defined using __lt__. The built-in sort is one
such method. So for example, if pList is a list composed of elements of type
Person, the call pList.sort() will sort that list using the __lt__ method
defined in class Person. \n''')

print('''
The following code: \n''')


print('''
pList = [me, him, her]
for p in pList:
    print(p)
pList.sort()
for p in pList:
    print(p)\n''')

print('''
will print: \n''')

pList = [me, him, her]
for p in pList:
    print(p)

print('''
and then print: 
''')

pList.sort()
for p in pList:
    print(p)
