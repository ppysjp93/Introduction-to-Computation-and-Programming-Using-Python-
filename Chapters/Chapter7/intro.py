print("################################################################################") 
print("""
INTRODUCTION\n""")
print("################################################################################") 

print("""
An "exception" is usually defined as "something that does not conform t othe
norm," and therefore somewhat rare. There is nothing rare about exceptions in
Python. They are everywhere. Virtually every module in the standarrd Python
library uses them, and Python itself will raise them in many ifferent
circumstances. You've already seen some of them. 
Open a python shell and type the following:\n""")

print("""
test = [1, 2, 3]
test[3]\n""")

print("""
You should find that you get an IndexError. IndexError is the type of exception
that Python raises when a program tries to access an element that is outside the
bounds of an indexable type. The string follwing IndexError provides additional
information about what caused the exception to occur. 
Most of the built-in exceptions of Python deal with situations in which a 
program has attempted to execute a stateement with no appropriate semantics. (We
will deal with the exceptional eceptions--those that do not deal with
errros--later in this chapter.) Thos readers (all of you, we hope) who have
attempted to write and run Python programs will already have encountered many of
these. Among the most commonly occurring types of exceptions are TypeError,
IndexError, NameError, and ValueError.\n""")
