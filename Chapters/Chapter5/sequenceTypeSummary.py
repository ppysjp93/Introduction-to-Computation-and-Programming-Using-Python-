print("################################################################################") 
print("""
SEQUENCE TYPE SUMMARY\n""")
print("################################################################################") 

print("""
The similaritees between str, tuple, range and list are as follows:
    * seq[i] returns the ith element of the sequence.
    * len(seq) returns the length of the equence.
    * seq1 + seq2 rturns the concatenation of the two seqences (not for ranges)
    * n*seq retruns a sequence tha repeaats seq n times (not for ranges)
    * seq[start:end] returns a slice of the sequence.
    * e in seq is True if e is contained in the sequence and False otherwise.
    * e not in seq is True if e is not in the sequence and False otherwise.
    * for e in seq iterates over the elemetns of the sequence.\n""")

print("""
The key differences between str, tuple, range and list is this:
    * lists are mutable, whilst the rest of the types are not. j\n""")

print("""
It is this fact that means that Python programmers to tend to use lists far 
more often than tuples. Since lists are mutable, they can be constructed
incremently during a computation. For example, the follwing code incremntally
builds a list containing all of the evenin numbers in another list.\n""")

evenElems = []
L = [2, 3, 4, 5, 6, 7]
for e in L:
    if e%2 in L:
        evenElems.append(e)

print("""
One advantage of tuples is that because they are immmutable, aliasing is never 
a worry. Another advantage of their being immutable is that tuplese, unlike 
list can be used as keys in dictionaries, as we will see in the next section.
Since strings can contain only characters, they are considerably less versatile
than tuples or lists. On the other hand, when you are working with a string of
characters there are many built-in methods that make life easy. Below contains
short description of a few of them. Rememer strings are IMMUTABLE so the below
are all values and have no side effect. 
One in method that is particularly is split, which takes two strings as
arguments. The second argument specifies a separator that is used to split the
first argument into a sequence of substirngs: 
It is this fact that means that Python programmers to tend to use lists far 
more often than tuples. Since lists are mutable, they can be constructed
incremently during a computation. For example, the follwing code incremntally
builds a list containing all of the evenin numbers in another list.\n""")

print("""
print('My favorite professor--John G.--rocks'.split(' '))
print('My favorite professor--John G.--rocks'.split('-'))
print('My favorite professor--John G.--rocks'.split('--'))\n""")


print('My favorite professor--John G.--rocks'.split(' '))
print('My favorite professor--John G.--rocks'.split('-'))
print('My favorite professor--John G.--rocks'.split('--'))

print("\nSTRING METHODS")

print("""
* s.count(s1) counts how many times the string s1 occurs in s.
* s.find(s1) retuns the index of the first occurrence of the substring s1 in s, 
    and -1 if s1 is not in s.
* s.rfind(s1) same as find, but starts from the end of s (the "r" in rfind
        stands for reverse).
* s.index(s1) same as find, but raises an exception if s1 is not in s.
* s.rindex(s1) same as indexx, but starts from the end of s.
* s.lower() converts all uppercase letters in s to lowercase
* s.replace(old,new) replaces all occurences of the string old in s with the
    string new.
* s.rstrip() removes trailing white space from s.
* s.split(d) (see Example above) \n""")



