def IsOdd(integer):
    if integer % 2 == 1:
        return True
    else: 
        return False

print('Please enter 10 integers')

i = 10
highestOdd = 1
n = 1 

while i != 0:
    print('Integer', n, ': ')    
    testInt = int(input()) 
    if testInt > highestOdd and IsOdd(testInt):
        highestOdd = testInt
    i = i - 1 
    n = n + 1

print("\nhighestOdd = \n", str(highestOdd))


    
