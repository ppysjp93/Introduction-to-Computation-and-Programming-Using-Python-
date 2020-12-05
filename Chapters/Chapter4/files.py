print("################################################################################") 
print("""
FILES""")
print("################################################################################") 

print("""
Python handles findles by using somethin called a file handle. """)

nameHandle = open('kids', 'w')

print("""
The above code instructs the operating system to create a file with the name
kids and return a file hand for that file. The 'w'w to pen indicates that the
file is to be opened for writing. The following code opens a file uses the write
method to write two lines, and the n closes the file. It is important to
remember to close the file when the program is finsihed using it.Otherwise
there is a risk that some or all of the writes may not be saved.""")

print("""
nameHandle = open('kids', 'w')
for i in range(2):
    name = input('Enter name: ')
    nameHandle.write(name + '\\n')
nameHandle.close()""")

def writeNamesToKids(n):
    nameHandle = open('kids', 'w')
    for i in range(n):
        name = input('Enter name: ')
        nameHandle.write(name + '\n')
    nameHandle.close()

writeNamesToKids(2)

print("""
The 'kids' file can now be opened for reading and print its contents. Since
Python treats a file as a sequence of lines, we can use a for statement to
iterate over the file's contents. """)

print("""
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)
nameHandle.close()
""")

def readFile():
    nameHandle = open('kids', 'r')
    for line in nameHandle:
        print(line)
    nameHandle.close()

readFile()
print("""
Enter the names David and Andrea this time:""")

writeNamesToKids(2)

readFile()

print("""
The extra line appears but if we adjust the print so that it prints line[:-1] 
then it will skip the '\\n' special character. Here is how you would do this:""")

print("""
nameHandle = open('kids', 'w')
nameHandle.write('Micheal\n')
nameHandle.write('Mark\n')
nameHandle.close()
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()""")

nameHandle = open('kids', 'w')
nameHandle.write('Micheal\n')
nameHandle.write('Mark\n')
nameHandle.close()
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()

print("""
This will print Micheal and Mark without a space between the lines. The is a 
list of commands you can use with file handlers on page 63. Finally you will
probably want to use the argument 'a' instead of 'w' as 'a' appends to a file
and doesn't delete its contents whilst 'w' deletes the contents of a file and
then writes into it.""")




