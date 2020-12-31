# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    count = 0
    for letter in letters_guessed:
        count += secret_word.count(letter)
        
    if count == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    i = 0
    letters_guessed_dict = {} 
    for char in secret_word:
        for letter in letters_guessed:
            if char == letter:
                letters_guessed_dict[i] = letter
        i += 1 
        
    guessed_so_far = ""
    j = 0
    while j < len(secret_word):
        s = letters_guessed_dict.get(j, "_ ")
        guessed_so_far += s 
        j += 1
        
    return guessed_so_far



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    remove_letters_dict = {}
    for letter in letters_guessed:
        i = 0
        for char in string.ascii_lowercase:
            if letter == char:
                remove_letters_dict[i] = letter 
            i += 1
    
    available_letters = "" 
    i = 0 
    for letter in string.ascii_lowercase:
        if remove_letters_dict.get(i, "") == letter:
            i += 1 # still needs to increment otherwise will be out of sync
            continue 
        else:
            available_letters += letter
        i += 1
            
    return available_letters
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    letters_guessed = []
    num_Guesses = 6
    available_letters = get_available_letters(letters_guessed)
    num_Warnings = 3
    with_Hints = False
    print("""
      Welcome to the game Hangman! 
      I am thinking of a word that is {0} letters long.
      You have {1} warnings left.
      --------------------------------------
      """.format(len(secret_word),num_Warnings))
    
    while not is_word_guessed(secret_word, letters_guessed) and num_Guesses != 0:       
        begin_round(num_Guesses,available_letters)       
        guess = str.lower(input("Please guess a letter: "))       
        num_Guesses, num_Warnings, valid_guess = is_invalid_guess(guess, \
                                            letters_guessed, secret_word,\
                                            num_Warnings,num_Guesses, with_Hints)    
            
        if not valid_guess:
            continue     
        
        letters_guessed.append(guess)        
        available_letters = get_available_letters(letters_guessed)         
        num_Guesses = guess_in_secret_word(guess, secret_word, num_Guesses, letters_guessed)        

        
    game_won_or_lost(num_Guesses,secret_word)
    
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def is_invalid_guess(guess, letters_guessed, secret_word, num_Warnings, \
                     num_Guesses, with_Hints):
    
        s1 = ''
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        
        if not is_guess_alpha(guess):           
            valid_guess = False      
            num_Warnings = update_warnings(num_Warnings)
            s1 = "Opps that is not a valid letter."
                
        elif is_guess_in_letters_guessed(guess, letters_guessed):
            
            valid_guess = False
            num_Warnings = update_warnings(num_Warnings)
            s1 = "Oops you have already guessed that letters."     
                
        else:
            valid_guess = True 
        
        s2 = ''
        
        if not valid_guess:
            if guess == "*" and with_Hints:
                print("Possible word matches are: ")
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                s1 = ''
            elif num_Warnings < 0:
                s2 = "You have no warnings left so you lose one guess: {0}".format(guessed_word)
                num_Warnings = 3
                num_Guesses -= 1
            else:
                s2 = "You have {0} warnings left: {1}".format(num_Warnings,guessed_word)
                
            print(s1 + s2)
            print("------------------------------------------------------------")

        return num_Guesses, num_Warnings, valid_guess


def begin_round(num_Guesses,available_letters):
    print("""
    You have {0} guesses left.
    Available letters: {1}
    """.format(num_Guesses,available_letters))
    

def update_warnings(num_Warnings):
    num_Warnings -= 1
    return num_Warnings

def update_guesses(num_Guesses):
    num_Guesses -= 1
    return num_Guesses

def is_guess_in_letters_guessed(guess, letters_guessed):
    if guess in letters_guessed:
        return True
    else:
        return False
    
def update_num_Guesses_vowel(guess,num_Guesses):
    if guess in ('a', 'e', 'i','o','u'):
        num_Guesses -= 1
        return num_Guesses
    else:
        return num_Guesses

def guess_in_secret_word(guess, secret_word, num_Guesses, letters_guessed):
    if guess not in secret_word:
        num_Guesses = update_num_Guesses_vowel(guess, num_Guesses)
        num_Guesses -= 1
        print("Oops! That letter is not in my word: {0}"\
                  .format(get_guessed_word(secret_word, letters_guessed)))
        print("------------------------------------------------------------")
        return num_Guesses
    else:
        print("Good Guess: {0}"\
                  .format(get_guessed_word(secret_word, letters_guessed)))
        print("------------------------------------------------------------")
        return num_Guesses
    
def game_won_or_lost(num_Guesses, secret_word):
    if num_Guesses == 0:
        print("Sorry you ran out of guesses. The word was '{0}'.".format(secret_word))
    else:
        print("Congratulations! You win!\
              \nYour total score for this game is: {0}".format(total_score(\
                                                      secret_word, num_Guesses)))
        
        
def num_unique_letters(secret_word):
    return len(''.join(set(secret_word)))

def total_score(secret_word, num_Guesses):
    unique_letters = num_unique_letters(secret_word)
    return unique_letters*num_Guesses

def is_guess_alpha(guess):
    if len(guess) == 1 and str.isalpha(guess):
        return True
    else:
        return False


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_no_spaces = my_word.replace(" ","")
    words_eq_len = len(my_word_no_spaces) == len(other_word)
    
    if words_eq_len:

        already_tested = {}
        
        for i in range(len(my_word_no_spaces)):   
            if key_not_match_val(my_word_no_spaces[i],other_word[i]) and my_word_no_spaces[i] != '_':
                return False
            else:
                already_tested[my_word_no_spaces[i]] = other_word[i]
                
        if len(already_tested) == len(my_word_no_spaces):
            return False
        else:
            return True
        
    else:
        return False

def key_not_match_val(key,val):
    return key != val

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches = ""
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            matches += other_word + " "
    
    if matches == "":
        print("No matches found.")
    else:
        print(matches)

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    num_Guesses = 6
    available_letters = get_available_letters(letters_guessed)
    num_Warnings = 3
    with_Hints = True
    
    print("""
      Welcome to the game Hangman! 
      I am thinking of a word that is {0} letters long.
      You have {1} warnings left.
      --------------------------------------
      """.format(len(secret_word),num_Warnings))
    
    while not is_word_guessed(secret_word, letters_guessed) and num_Guesses != 0:       
        begin_round(num_Guesses,available_letters)       
        guess = str.lower(input("Please guess a letter: "))       
        num_Guesses, num_Warnings, valid_guess = is_invalid_guess(guess, \
                                            letters_guessed, secret_word,\
                                            num_Warnings,num_Guesses, with_Hints)    
            
        if not valid_guess:
            continue
        

            
        
        letters_guessed.append(guess)        
        available_letters = get_available_letters(letters_guessed)         
        num_Guesses = guess_in_secret_word(guess, secret_word, num_Guesses, letters_guessed)        

        
    game_won_or_lost(num_Guesses,secret_word)





# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    # win test
    #secret_word = 'tact'
    # lose test
    #secret_word = 'else'    
    #hangman(secret_word)
    
    
    my_word = "a_ ple"
    other_word = "apple"
    print("my_word: {0}".format(my_word))
    print("other_word: {0}".format(other_word))
    print("result: {0}".format(match_with_gaps(my_word, other_word)))
    
    
    # secret_word = 'apple'
    # letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    # #letters_guessed = ['a', 'p', 'l', 'e']
    # print(is_word_guessed(secret_word, letters_guessed))
    # print(get_guessed_word(secret_word, letters_guessed))
    # print(get_available_letters(letters_guessed))
    
###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    #secret_word = "apple"
    hangman_with_hints(secret_word)
