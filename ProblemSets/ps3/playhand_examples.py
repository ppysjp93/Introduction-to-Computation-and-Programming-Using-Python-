# coding: utf-8
from ps3 import *

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

word_list = load_words()

print('''
Enter the words "jar" and "f*x" for the first example\n''')

hand = {'a': 1, 'j': 1, 'e': 1, 'f': 1, '*': 1, 'r': 1, 'x': 1}
play_hand(hand, word_list)

print('''
Enter the words "fix" and "ac" and "*t" for the second example\n''')

hand = {'a': 1, 'c': 1, 'f': 1, 'i': 1, '*': 1, 't': 1, 'x': 1}
play_hand(hand, word_list)
