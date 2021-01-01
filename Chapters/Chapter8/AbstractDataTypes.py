print("################################################################################") 
print('''
ABSTRACT DATA TYPES AND CLASSES\n''')
print("################################################################################") 

print('''
An abstract data type is a set of objects and the operations on those objects.
These are bound together so that one can pass an object from part of a program
to another, and in doing so provide access not only to the data attributes of
the object but also operations that ake it easy to manipulate that data.\n''')

print('''
The specifations of those operations define an interface between the abstract
data type and th erest of hte program. The interface defines the behavior of the
operations-what they do, but not how they do it. The interface therefore
provides an abstract barrier that isoloates the rest of hte program from the
data structures, algorithms, and code involved in providing a realization of hte
type of abstraction. \n''')

print('''
Programming is about managing complexity in a way that facilitates change. There
are 2 powerful mechanism available for accomplishing this: decomposition and
abstraction. Decomposition creates structure in a program, and abstraction
suppresses detail. The key is to suppress the appropriate details. This is what
data abstraction is for. Hopefully, these types capture concepts that will be
relevant over the lifetime of a program. If one starts the programming process
by devising types that will be relevant months and even decades later, one has a
great leg up in maintaining that software. \n''')

print('''
We have been using abstract data types (without calling them that) throughout
this book. We have written programs using intgers, lists, floats, strings and
dictionaries without giving any thought how these types might be implemented. To
paraphrase Moliere's Bourgeois Gentillhomme, "Par ma foi, il y a plus de cent
pages que nous avons utiliese ADTs, sans que nous le sachions." ("Good heavens,
for more than one hundred pages we have been using ADTs without knowing
it.")\n''')

print('''
In python one implements data abstractions using classes. In a moment we are
going to see a class definition which provides a straightforward implementation
of a set of-integers abstraction called IntSet. 
A class definition creates an object of type type and associates with that class
object a set of objects of type instancemethod. For example, the expression
IntSet.insert referes to the method insert defined in the definition of the
class IntSet. And the code:
    print(type(IntSet), type(IntSet.insert))
will print:
    <class 'type'> <class 'function'>
Notice how the docstring contains information about the abstraction provided by
the class, not information about how the class is implemented. In contrast the
comments below the specification contain information about hte implementation.
That inforation is aimed at pogrammer who might want to modif the implementation
or build subclasses of the classs. These are not for the programmer that just
wants to use the abstraction. \n''')

print('''
Let's now view the implementation of IntSet:\n''')

print('''
class IntSet(object):
    """
    An intSet is a set of integers
    """
    #Information about the implementation(not the abstraction)
    #Value of the set is represented by  a list of ints, self.vals. 
    #Each int in the set occurs in self.vals exactly once. 

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = [] 

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """
        Assumes e is an integer and removes e from self 
        Raises ValueError if e is not in self
        """
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def getMembers(self):
            """
            Returns a list containing the elements of self.
            Nothing can be assued about the order of the elements
            """
            return self.vals[:]

    def __str__(self):
            """
            Returns a string representation of self
            """
            self.vals.sort()
            result = ''
            for e in self.vals:
                result = result + str(e) + ','
            return '{' + result[:-1] + '}' #-1 omits trailing comma
''')

class IntSet(object):
    """
    An intSet is a set of integers
    """
    #Information about the implementation(not the abstraction)
    #Value of the set is represented by  a list of ints, self.vals. 
    #Each int in the set occurs in self.vals exactly once. 

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = [] 

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """
        Assumes e is an integer and removes e from self 
        Raises ValueError if e is not in self
        """
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def getMembers(self):
            """
            Returns a list containing the elements of self.
            Nothing can be assued about the order of the elements
            """
            return self.vals[:]

    def __str__(self):
            """
            Returns a string representation of self
            """
            self.vals.sort()
            result = ''
            for e in self.vals:
                result = result + str(e) + ','
            return '{' + result[:-1] + '}' #-1 omits trailing comma

print('''
Now that we have defined our new class IntSet let's talk about some terminolgy
which will help us when we are discussing object oriented programming.\n''')

print('''
When a function is defined within a class, then this function is called a
method and is associated with the class. These methods are sometimes referred to
as method attributes of the class. 
Classes support two kinds of operations:
    * Instantiation is sued to create instances of the class. For example, the
        statemnt s = IntSet() creates a new object of type IntSet. This object is
        called an instance of IntSet.
    * Attribute references use dot notation to access attributes associated with
        the class. For example, s.member refers to the method member associated with
        the instance s of type IntSet.\n''')

print('''
Each class definition begins with the reserved word class followed by the name
of the class and some information about how ti relates to other classes. In this
case, the first line indicates that IntSet is a subclass of object. For now,
ignore what it means to be a subclass. \n''')

print('''
We now consider our first special dunder method __init__. This method is called
whenever a class is instanciated. __init__ with the newly created object as teh
actual parameter that is bound to the formal parameter self. When invoked,
IntSet.__init__ creates vals, an object of type list, which becomes part of the
new created instance of type IntSet. (The list is created using the by now
familiar notation [], which is simply an abbreviation for list().) This
list is called a data attribute of the instance of IntSet. Notice that each
object of type IntSet will have a different vals list, as one would expect.
\n''')

print('''
As we have seen, method associated with an instance of a class can be invoked
using dot notation, see the following example:\n''')

print('''
s = IntSet()
s.insert(3)
print(s.member(3))\n''')


s = IntSet()
s.insert(3)
print("Prints: {0}".format(s.member(3)))

print('''
An artifact of the dot notation is that it looks as the when for example the
member method was called, it was called with too few arguments. This is because
the object associated with the expression preceding the dot is implicitly passed
as the first parameter to the method. This means we don't get code being written
that looks something like this: \n''')

print('''
s = IntSet()
self = s 
s.insert(s, 3)
print("Prints: {0}".format(s.member(3)))\n''')

print('''
In fact this doesn't make sense to the python interpreter as it makes it think
that s is being passed to the insert method twice, meaning it thinks that there
are in fact 3 arguments being passed to it instead of 2. \n''')

print('''
Using self as the name of the formal paramaeter is the normal convention Python
programmers use. A convention you should follow. \n''')

print('''
A class should not be confused with instances of that class, just as an object
of type list should not be confused dwith the list type. Attributes can be
associated either with a class itself or with instances of a class: 

    * Method attributes are defined in a class definition, for example
      IntSet.memeber is an attribute of the class IntSet. When the class is
      instantiated, e.g., by the statement s = IntSet(), instance attributes,
      e.g., s.member, are created. Keep in mind that IntSet.member and
      s.member are different object. While s.member is initially bound to the
      member method defined in the class IntSet, that binding can be changed
      during the course of a computation. For example, you could (but you
      shouldn't!) write s.member = InSet.insert.

    * When data attributes are associated with a class we call them class
      variables. When they are associated with an instance we call them instance
      variables. For example, vals is an instance variable becuase for each
      instance of class IntSet, vals is bound to a different list. So we haven't
      seen a class variable.\n''')

print('''
Data abstraction achieves representation-independence. Think of the
implementation of an abstract type as having several components:
    
    * Implementations of the methods of the type,

    * Data structures that together encode values of the type, and 

    * Conventions about how the implementations of the methods are to use the
      data structures. A key convention is captured by the representation
      invariant.\n''')

print("\nREPRESENTATION INVARIANT")

print('''
The representaiton invariant defines which values of the data attributes
correspond to valid representaiton of class instances. The representation
invariant for InSet is that vals contains no duplicates. The implementation of
__init__ is responsible for establishing the invariant (which holds on the empty
list, and the other methods are responsible for maintaining that
invariant.That is why insert appends e only if it is not already in
self.vals.\n''')

print('''
The implementation of remove exploits the assumption that the representation
invariant is satisfied when remove is entered. It calls list.remove only once, 
since the representation invariant guarantees that there is at most one
occurence of e in self.vals.\n''')

print('''
Another special method we come accross is the __str__ method. When the print
comman is used, the __str__ function associated with the object to be printied
is automatically invoked, as follows:\n''')

print('''
s = IntSet()
s.insert(3)
s.insert(4)
print(s)\n''')


s = IntSet()
s.insert(3)
s.insert(4)
print("Will print: ", s)

print('''
The dunder hash method allows you change how the hash value of the object is
calculated, if it is not provided then it defaults to the value derived from the
function 'id'. A user defined hash should make sure that the its value doesn't
change for the lifetime of that object.
The dunder __eq__ method needs to be provided otherwise all objects are
considered unequal except to them selves. \n''')
 
