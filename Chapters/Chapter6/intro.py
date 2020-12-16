print("################################################################################") 
print("""
TESTING AND DEBUGGING\n""")
print("################################################################################") 

print("""
Programs don't always function properly the first time we run them. Working out
where the problems are coming from is challenging, but there are a set of
principles which can be used to get complex systems to work. 'Testing' is the
process of running a porgram and trying to work out if it is doing what we are
expecting it to. Debugging is the process of trying to fix the program you know
doesn't work as intended. The best way to get your program to work is
modularity. We break up the program into separate components which can be
implemented, tested and debugged independently. In this chapter we are going to
focus on using functions. The first step is eliminating synax errors and static
semantic errors that can be detected without running the program. \n""")

print("\nTESTING")

print("""
The purpose of testing is to show that bugs exist, NOT to show that a program is
bug free. As Albert Einstein said, 'No ammount of experimentation can ever prove
me right; a single experiment can prove me wrong." The key to testing is to try
and find a 'test suite', which are a set of inputs that have a high likely hood
of revealing bugs. 
A partition of a set, divides the set into a collection of subsets such that
each element of the original set belongs to exactly one of the subsets.
Consider the function below: \n""")

print('''
def isBigger(x, y):
    """Assumes x and y are int
    Returns True if x is less than y and False otherwise.
    """\n''')


print("""
We can partition all integers into seven sets:

1)   x positive, y positive,
2)   x negative, y positive,
3)   x positive, y negative,
4)   x negative, y negative,
5)   x == 0, y != 0,
6)   x != 0, y == 0,
7)   x != 0, x != 0,\n""")

print("""
A heuristic is a sub-optimal way to problem solvem, which is sufficient and 
pragmatic. A heuristic based on exploring the paths through the code is called
'glass-box' testing. Heuristics based on exploring paths through the
specification fall into the class of black-box testing.\n""")


