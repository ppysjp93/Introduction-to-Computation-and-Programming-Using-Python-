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
for e in L:
    if e%2 in L:
        evenElems.append(e)

