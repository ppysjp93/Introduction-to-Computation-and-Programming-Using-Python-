WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


VOWELS = 'aeiou'

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word_dict = {}
    word = str.lower(word)

    for letter in word:
        if letter not in word_dict:
            word_dict[letter] = 1
        else:
            word_dict[letter] += 1    
        
    valid_number_letters = True # Flag 1

    for key in word_dict:
        if key not in hand:
            return False
        elif hand[key] < word_dict[key]:
            valid_number_letters = False

    wildcard_position = word.find('*')
    word_in_word_list = False # Flag 2

    if wildcard_position == -1:
        word_in_word_list = word in word_list
    else:
        for vowel in VOWELS:
            test_word = word[:wildcard_position] + vowel + word[wildcard_position+1:]
            if test_word in word_list:
                word_in_word_list = True

    if not word_in_word_list or not valid_number_letters:
        return False
    else:
        return True



#
word_list = load_words()
word = 'e*m'
hand = {'a': 1, 'r': 1, 'e':1, 'j': 2, 'm': 1, '*': 1}

#word = 'c*wz'
#hand = {'c':1, 'o':1, '*':1, 'w': 1, 's':1, 'z': 1, 'y': 2}

print(is_valid_word(word, hand, word_list))


