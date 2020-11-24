print("################################################################################") 
print("""
USING FLOATS """)
print("################################################################################") 

print("""
Floats don't always reflect real numbers and this is something that you should 
be aware of.  Try the code below: """)

x = 0.0
for i in range(10):
    x = x + 0.1 
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, ' is not 1.0')

print("""
In almost all modern programming languages non-integer numbers are implemented 
using a representation called floating point. For the moment, let's pretend
that the internal representation is in decimal. We would represent a number as a 
pair of integers- the signigicant digits of the number and an exponent. For 
example, the number 1.949 would be represented as the pai (1949, -3) which 
stands for the product 1949e-3.
The number of significant digits determines the precision with which numbers can
be represented. If for example, the number 1.949 there were only two significant
digits, the number 1.949 could not be represented exactly. It would have to be 
converted to some approximation of 1.949, in this case 1.9. This approximation 
is called the rounded value. Modern computers use binary, not decimal 
representations. We represent the significant digits  and exponents in binary 
rather than decimal and raise 2 rather than 10 to the exponent. For example, the
number 0.625 (5/8) would be represented as the pair (101, -11) because 5/8 is 
0.101 in binary and -11 is the binary representation of 03, the pair (101, -11)
stands for 5*2^-3 = 5 / 8 = 0.625. 
What about the decimal fraction 1/10, which we write in Python as 0.1? The best
we can do with four significant binary digits is (0011, -101) = 0.00011. This 
is equivalent to 3/32, i.e., 0.09375. If we had five sginificant binary digits,
we would repreent 0.1 as (11001, -1000), which is equivalent to 25/256, i.e. 
0.09765625. How many significant digits would we need to get an exact floating
point representation of 0.1? An infinite number of digits! There do not exist
integers sig and exp such that sig*2^-exp  equals 0.1. So we are in a bit of a 
bind. the best we an do is represent 0.1 to approximate 0.1. In most Python 
implementations there are 53 bits of precision available for floating point 
numbers, so the significant digits stored for the decimal 0.1 will be: 
   110011001100110011001100110011001100110011001 
This is equivalent to: 
   0.10000000000000000555111512312578270211815834045541015625
Pretty close but not exact. Hopefully this should now explain why the above code
doesn't act as expected. Where this understanding is most important is when we 
are creating are tests when dealing with floating point numbers. It is much 
better to write a test like abs(x-y) < 0.0001 than x == y when we are using 
floating points. """)

