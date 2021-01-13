print("################################################################################") 
print("""
CONDUCTING TESTS \n""")
print("################################################################################") 
 
print("""
Testing is often thought of as occurring in two phases. One should always start
with unit testing. During this phase testers construct and run tests desingned
to ascertain whether individual units of code work properly. This is then
followed by 'integration testing' which is designed to ascertain wheter the
program as a whole behaves as intended. In practice, testers cycle through these
two phases, sign failures during integration testing lead to making changes to
individual units.\n""")

print("""
Integration testing is almost always more challenging than unit testing. One
reason for this is that the intended behavior of an entire program is often
considerably harder to characterize than the intended behavior of its parts.
Problems of scale are alo a big factor. Integration tests can sometimes take
days to run.\n""")

print("""
Most testing is highly automated. People use test drivers that autonomously:
    * Set up theenvironment needed to invoke the unit to be tested,
    * Invoke the program with a predefined set of generated inputs.
    * Save the results of these invocations,
    * Check the acceptability of the reuslts of the tests, and
    * Prepare an appropriate report. \n""")

print("""
During unit testing we often need to build 'stubs' as well as drivers. Drivers
simulate parts of the program that use the unit being tested, whereass stubs
simulate parts of the program used by the unit being tested. Stubs are useful
because they allow people to test untis that depend upon software or sometimes
even hardware that does not yet exist. This allows team of programmers to
simultaneously develop and test multiple parts of a system. 
Ideally a stub should: 
    * Check the reasonableness of the envrionment and arguments supplied by the
        caller (calling a function wiht inappropriate arguments is a common error),
    * Modify the arguments and global variables in a manner consistent with the
        specification, and 
Most testing is highly automated. People use test drivers that autonomously:
    * Set up the environment needed to invoke the unit to be tested,
    * Invoke the program with a predefined set of generated inputs.
    * Save the results of these invocations,
    * Check the acceptability of the reuslts of the tests, and
    * Prepare an appropriate report. 
    * Return values consistent with the speciication.\n""")

print('''
Building adequate stubs is often a challenge. If the unit the stub is replacing
is intended to perform some complex task, building a stub that performs actions
consisten with the specification may be tantamout to writing the program that
the stub is designed to replace. One way to surmount htis problem is to limit
the set of arugments accepted by the stub, and create a table that contains the
values to be returned for each combination of a arguments to be used in the test
suite.
One attraction of automating the testing process is that it facilitates
regression testing. As programmers attempt ot debug a program, it is all to
common to install a "fix" that breaks something that used to work. Whenever any
change is made not matter how small, you should check that the program still
passes all of the test that it used to pass.\n''')


