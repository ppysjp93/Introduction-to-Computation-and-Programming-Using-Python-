print("################################################################################") 
print("""
DICTIONARIES\n""")
print("################################################################################") 

print("""
Objects of type dict (short for dictionary) are like lists except what we 
index them using keys. Think of a dictionary as a set of key/value pairs.
Literals of type dict are enclosed in curly braces, and each element is written
as a key followed by a oclon followed by a value. For example, the code:\n""")

print("""
monthNumber = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb',
        3:'Mar', 4:'Apr', 5:'May'}\n""")

monthNumber = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb',
        3:'Mar', 4:'Apr', 5:'May'}

print("""
print('The third month is ' + monthNumber[3])
dist = monthNumber['Apr'] - monthNumber['Jan']
print('Apr and Jan are', dist, 'months apart')
print(monthNumber[1])\n""")

print('The third month is ' + monthNumber[3])
dist = monthNumber['Apr'] - monthNumber['Jan']
print('Apr and Jan are', dist, 'months apart')
print(monthNumber[1])

print("""
The entries in a dict are unordered and cannot be accessed with an index. That's
why monthNumbers[1] unambiguously refers to the entry with the key 1 rather than
the second entry.\n""")

print("""
Lke lists, dictionaries are mutable. We can add an entry by writing

monthNumber['June'] = 6 

or change an entry by writing

monthNumber['May'] = 'V' \n""")

monthNumber['June'] = 6 
monthNumber['May'] = 'V' 

print(monthNumber)

print("""
Dictionaries are one of the great thinks about Python. They greatly reduce the
difficulty of writing a variety of programs. For example, in a moment, we use
dictionaries to write a (pretty horrible) program to translate between
languages. Since of the lines of code was too long to fit on the page, we used a
backslash, \ to indicate that the next line of text is a continuation of the
previous line.\n""")

print("""
 EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je', 'eat':'mange',
        'drink':'bois', 'John':'Jean', 'friends':'amis', 'and': 'et', 'of':'du',
        'red':'rouge'}

FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I', 'mange':'eat',
        'bois':'drink', 'Jean':'John', 'amis':'friends', 'et':'and', 'du':'of',
        'rouge':'red'}

dicts = {'English to French':EtoF, 'French to English':FtoE}""")

EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je', 'eat':'mange',
        'drink':'bois', 'John':'Jean', 'friends':'amis', 'and': 'et', 'of':'du',
        'red':'rouge'}

FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I', 'mange':'eat',
        'bois':'drink', 'Jean':'John', 'amis':'friends', 'et':'and', 'du':'of',
        'rouge':'red'}

print("""
dicts = {'English to French':EtoF, 'French to English':FtoE}

def translateWord(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word


def translate(phrase, dicts, direction):
    UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCLetters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCLetters + LCLetters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        else:
            translation = translation\
                    + translateWord(word, dictionary) + c
            word = ''
    return translation + ' ' + translateWord(word, dictionary)""")
        
dicts = {'English to French':EtoF, 'French to English':FtoE}

def translateWord(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word


def translate(phrase, dicts, direction):
    UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCLetters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCLetters + LCLetters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        else:
            translation = translation\
                    + translateWord(word, dictionary) + c
            word = ''
    return translation + ' ' + translateWord(word, dictionary)

print("\nHere is the code put to action:")
print("\n",translate('I drink good red wine, and eat bread.',
    dicts, 'English to French'))

print("\n",translate('Je bois du vin rouge.',
    dicts, 'French to English'))



print("""
A for statement can be used to iterate over the entries ina dictionary. However,
the value assigned to the interation variables is a key, not a key/value pair.
The order in which th ekeys are seen in the iteration is not defined. For
example the code:\n""")


print("""
monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb',
                3:'Mar', 4:'Apr', 5:'May'}\n""")

print("""
keys =[]
for e in monthNumbers:
    keys.append(str(e))
print(keys)
keys.sort()
print(keys)\n""")

print("""
might print \n""")

print("""
['Jan', 'Mar', '2', '3', '4', '5', '1', 'Feb', 'May', 'Apr']
['1', '2', '3', '4', '5', 'Apr', 'Feb', 'Jan', 'Mar', 'May']\n""")

print("""
it in fact prints: \n""")

monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb',
                3:'Mar', 4:'Apr', 5:'May'}

keys =[]
for e in monthNumbers:
    keys.append(str(e))
print(keys)
keys.sort()
print(keys)

print("""
The key thing to notice here is that when the dictionary is iterated through, it
is a key that is appened NOT a key value pair. The order in whihc the keys are
seen in the iterations is not defined, which explains the somewhat random
ordering of what is printed above. That is the key you should take away from
what you have just read.\n""")

print("""
In the next example we are going to see how the method 'keys' returns a
dict_keys object. The order in which the keys appear in the view is not defined.
A view obejct is dynamic in that if the obejct with which it is associated
changes, the change is visible through the view object. For example, \n""")

birthStones = {'Jan':'Garnet', 'Feb':'Amethyst', 'Mar':'Acquamarine',
                'Apr':'Diamon', 'May':'Emerald'}
print("""
months = birthStones.keys()
print(months)
birthStones['June'] = 'Pearl'
print(months)

might print

dict_keys(['Jan', 'Feb', 'May', 'Apr', 'Mar'])
dict_keys(['Jan', 'Mar', 'June', 'Feb', 'May', 'Apr'])

And it actually prints:
""")

months = birthStones.keys()
print(months)
birthStones['June'] = 'Pearl'
print(months)

print("""
Objects of type dict_keys can be iterated over using for, and membership can be
tested using in. An object of type dict_keys can easily be converted into a
list e.g., list(months).
Not all types of objects can be used as keys: A key must be an objet of a
'hashable type'. A type is hashable if it has \n""")

print("""
* A __hash__ method that maps an object of the type to an int, and for every
    object the value returned by __hash__ does not change during the lifetime of 
    the object, and
* An __eq__ method that is used to compare objects for equality.\n""")

print("""
All of Python's built-in immutable types are hashable, and none of Python's
built-in mutable types are hashable. It is often convenient to use tuples
askeys. Imagine, for example, using a tuple of the form (flightNumber, day)) to
represent airline flights, It would then ve easy to use such tuples as keys in a
dictionary implementing a mapping from flights to arrival times. As with lists,
there are many useful mehtods associated with dictionaries, including some for
removing elements. We do not enumerate all of them here, but will use them as
convenient in examples later in the book. There is a table on page 83 of the
useful things you can do with dictionaries.\n""")




