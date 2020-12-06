print("################################################################################") 
print("""
LISTS AND MUTABILITY\n""")
print("################################################################################") 

print("""
Like a tuple, a list is an ordered seuqnce of values where each value is 
identified by an index. The syntax for expressing literals of type list is
similar to that used for tuples; the difference is that we use square brackts
rather than parentheses. The epty list is written as [], and singleton lists are
written without that (easy to forget) comma before the closing brack. So, for
eample, the  code: """)

print("""
L = ['I did it all', 4 , 'love']
for i in range(len(L)):
    print(L[i])\n""")

print("""
produces the following output: \n""")

L = ['I did it all', 4 , 'love']
for i in range(len(L)):
    print(L[i])

print("""
Occasionally, the fact that square brackets are used for literals of type list,
indexing into lists, and slicing lists can lead to some visual confusion. For
example, the expressions [1,2,3,4],[1:3][1], which evaluates to 3, uses the
square brackets in three different ways. This is rarely a problem in practice,
because most of the time lists are built incrementally rather than written as
literals. """)

print("""
Lists differ from tuples in one hugely important way: lists are mutable. In
contrast tuples and strings are immutable. There are many operators that can be
used to create object of these immutable types, and variables can be bound to
object of these types. But objects of immutable types cannot be modified. On the
other hand, object of type list can be modified after tehy are created. The
distinction between mutating an object and assinging an object to a variable
may, at first, appear subtle, However, if you keep repeating the mantra, "In
Python a variable is merely a name" i.e., a lable that can be attached to an
object, it will bring you clarity.
Consider:""")
print("""
Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown]""")

Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']

print("""
the interpreter creates two new lists and binds the appropriate variables to
them as pictured on pagethe interpreter creates two new lists and binds the
appropriate variables to them as pictured on page 69.""")

print("""
The following assignment statements: 
Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
""")

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

print("\nUnivs = \n", str(Univs))
print("\nUnivs1 = \n", str(Univs1))
print("\nUnivs ==  Univs1\n", str(Univs == Univs1)) 

print("""
This is a case that makes it appear to be the case that Univs and Univs1 are
bound to the same value. This is VERY MUCH NOT the case. Try and draw a diagram
and check it against page 70 to see if you can see why this isn't the case.""")

print("""
Python has a built-in function which can be used to verify that Univs and Univs1
are bound to different objects: 'id' which returns a unique integer identifier
for an object. This function allows us to to test for 'object equality'""")

print("""
print(Univs == Univs1) #test value equality
print(id(Univs) == id(Univs1)) #test object equality
print('Id of Univs =', id(Univs))
print('Id of Univs1 =', id(Univs1))\n""")

print(Univs == Univs1) #test value equality
print(id(Univs) == id(Univs1)) #test object equality
print('Id of Univs =', id(Univs))
print('Id of Univs1 =', id(Univs1))


print('\nId of Univs[0] and Univs[1] =', id(Univs[0]), id(Univs[1]))
print('Id of Univs1[0] and Univs1[1] =', id(Univs1[0]), id(Univs1[1]))

print("""
So lets now use mutability and see what it does to our lists. We are now going
to mutate Techs by apending 'RPI' to it.
Techs.append('RPI')""")

Techs.append('RPI')

print("\nUnivs = \n", str(Univs))
print("\nUnivs1 = \n", str(Univs1))
print("\nUnivs ==  Univs1\n", str(Univs == Univs1)) 

print("""
This is an example of 'aliasing' which can be both convenient and treachorous.
There are two distinct paths to the same list object. One path is through the
variable Techs and the other through the first element of the list object to
which Univs is bound. One can muttate the object via either path, and the effect
of the mutation will be visible through both paths. Uniintentional aliasing lead
to programming errors that are often enormously hard to track down.""")

print("""
As with tuples, a for statement can be used to tierate over the elements of a
list. For example:""")

print("""
for e in Univs:
    print('Univs contains', e)
    print('  which contains')
    for u in e:
        print('   ', u)\n""")

for e in Univs:
    print('Univs contains', e)
    print('  which contains')
    for u in e:
        print('   ', u)

print("""
When we append one list to another, e.g., Techs.append(Ivys), the original
structure is maintained. I.e., the result is a list that contains a list.
Suppose we want to ad the elements of one list into another list. We can do that
by using list concatentation or the extend method e.g.,
""")

print("""
L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print('L3 =', L3)
L1.extend(L2)
print('L1 =', L1)
L1.append(L2)
print('L1 =', L1)\n""")

L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print('L3 =', L3)
L1.extend(L2)
print('L1 =', L1)
L1.append(L2)
print('L1 =', L1)

print("""
Notice that the operator '+' does not have a side effect. It creates a new list
and returns it. In contrast, extend and append each mutated L1.
Figure 5.4 contains short descriptions of somse of the methods associate with
lists. Note that all of these except count and index mutate the list (page 73). 
""")


