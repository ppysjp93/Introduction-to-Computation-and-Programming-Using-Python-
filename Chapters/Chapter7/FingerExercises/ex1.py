print("################################################################################") 
print("""
FINGER EXERCISE\n""")
print("################################################################################") 

print("""
Implement a function that meeters the specification below.\n""")

print('''
def sumDigits(s):
    """
    Assumes s is a string.
    Returns the sum of the decimal digits in s.
    For example, if s is 'a2b3c' it returns 5
    """\n''')


print('''
def sumDigits(s):
    """
    Assumes s is a string.
    Returns the sum of the decimal digits in s.
    For example, if s is 'a2b3c' it returns 5
    """
    sum_of_digits = 0 
    for letter in s:
        try:
            sum_of_digits += int(letter)
        except ValueError:
            print("{0} is not a number so not added".format(letter))
    return sum_of_digits\n''')

def sumDigits(s):
    """
    Assumes s is a string.
    Returns the sum of the decimal digits in s.
    For example, if s is 'a2b3c' it returns 5
    """
    sum_of_digits = 0 
    for letter in s:
        try:
            sum_of_digits += int(letter)
        except ValueError:
            print("{0} is not a number so not added".format(letter))
    return sum_of_digits

print("""
sumDigits('a2b3c')\n""")
sumDigits('a2b3c')
