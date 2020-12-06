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

