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

# exception may be needed here if none int is entered. 
number_of_hands = int(input('Enter total number of hands: ')) 
hands = []
for i in range(number_of_hands):
    hands.append(deal_hand(HAND_SIZE))

game_score = 0
for hand in hands:
    print('Current hand: ', end=' ')
    display_hand(hand)

    substitute_letter = input('Would you like to substitute a letter? ')
    if substitute_letter == 'yes':
        letter = input('Which letter would you like to replace? ')
        hand = substitute_hand(hand, letter)  
         
    game_score += play_hand(hand, word_list)
    print('----------')
