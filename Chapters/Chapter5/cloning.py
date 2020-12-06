print("################################################################################") 
print("""
CLONING\n""")
print("################################################################################") 

print("""
It is usually prudent to avoid mutating a list over which one is iterating. The 
following code: """)

print('''
def removeDups(L1, L2):
    """
    Assumes that L1 and L2 are lists. 
    Removes any element from L1 that also occurs in L2
    """
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)''')

def removeDups(L1, L2):
    """
    Assumes that L1 and L2 are lists. 
    Removes any element from L1 that also occurs in L2
    """
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)

print("""
L1 = [1,2,3,4]
L2 = [1,2,5,6]

removeDups(L1, L2)
""")

L1 = [1,2,3,4]
L2 = [1,2,5,6]

removeDups(L1, L2)
print('L1 =', L1)

print("""
You might be surprised to discover that the implementation of Python keeps track
of where it is in the list using an internal counter that is incremented at the
end of each iteration. When the value of the counter reaches the current length
of the list, the loop terminates. This works as one might expect if the list is
not mutated within the loop, but can have surprising consequences if the list is
mutated. In this case, the hidden counters out at 0, discovers that L1[0] is in
L2, and removes it reducing the length of L1 to 3. The counter is then
incremented to 1, and the code proceeds to check if the value of L1[1] is in L2.
Notice that this is not the iriginal value of L1[1] (i.e., 2) but rather the
current value of L1[1] (i.e., 3). As you can see, it is possible to figure out
what happens when the list is modified within the loop. However it is not easy.
And what happens in likely to be unintentional.
This is where slicing to 'clone' comes in. Slicing to clone is done by making a
copy of the list and write 'for e1 in L1[:]:'.
It's important to note that assigning a variable 'newL1' to L1 like below:
    newL1 = L1
and then iterating over this 'new' variable wouldn't work because 'newL1' is
just a name and is pointing at the same list L1.""")

print('''
def removeDups2(L1, L2):
    """
    Assumes that L1 and L2 are lists. 
    Removes any element from L1 that also occurs in L2
    """
    for e1 in L1[:]: # here is the clone by slicing of L1 -> L1[:]
        if e1 in L2:
            L1.remove(e1)''')

def removeDups2(L1, L2):
    """
    Assumes that L1 and L2 are lists. 
    Removes any element from L1 that also occurs in L2
    """
    for e1 in L1[:]: # here is the clone by slicing of L1 -> L1[:]
        if e1 in L2:
            L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]

removeDups2(L1, L2)
print('\nL1 =', L1)

print("""
This is now the expected result we are after!""")

print("""
Slicing is not the only way of making a clone in Python. The expression list(L)
retruns a copy of the list L. If the list to be copied contains mutable objects
that you want to copy as well, import the standard library module copy and use
the function copy.deepcopy.""")
