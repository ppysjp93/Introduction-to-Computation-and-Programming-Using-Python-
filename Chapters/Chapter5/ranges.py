print("################################################################################") 
print("""
RANGES\n""")
print("################################################################################") 

print("""
Like string and tuples, ranges are immutable. The range funciton returns an 
object of type range. As stated in Section 3.2, the range function takes three 
integer arguments: 'start', 'stop' and 'step' and returns the progression of 
integers start, start + step, start + 2*step ... and so on. If step is positive,
the last element is the largest integer start + i*step less than stop. If step
is negative, the last element is the smallest integer start + i*step greater
than stop. If only two arguments are supplied, a step of 1 is used. If only one
argument is supplied, that argument is the stop, start defaults to 0, and step
defualts to 1.
All of the operations on tuples aer also available for ranges, except for
conatenation and repitition. For example, range(10)[2:6][2] evaluates to 4. When
the == operator is sued to compare object of type range, it returns True if the
two ranges represent the samea sequence of integers. For example, range(0, 7, 2)
== range(0,8,2) evaluates to True. However, range(0,7,2) == range(6, -1, -2)
evaluates to False because though the ranges contain the same integers, they
occur in a different order.
Unlike objects of type tuple, the amount of space occupied by an object of
type range is not proportional to tis length. Because a range is fully defined 
by its start, stop and step values, it can be stored in a small amount of space.
The most common use of range is in for loops, but object of type range can be
used anywhere a sequence of integers can be used.""")
