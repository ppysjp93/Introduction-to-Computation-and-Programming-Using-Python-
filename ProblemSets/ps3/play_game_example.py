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

def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg + ' ')
        try:
            return(valType(val)) # convert string to val type before returning
        except ValueError:
            print(val, errorMsg)# exception may be needed here if none int is entered. 


number_of_hands = readVal(int, 'Enter total number of hands: ', 'is not a integer')

hands = []
for i in range(number_of_hands):
    hands.append(deal_hand(HAND_SIZE))

game_score = 0
i = 0
repeat_hand = False
sub_letter_bool = True
repeat_hand_bool = True
game_score_dict = {}

while i < len(hands):

    hand = hands[i].copy()

    print('Current Hand: ', end=' ')
    display_hand(hands[i])


    if sub_letter_bool:

        substitute_letter = input('Would you like to substitute a letter? ')

        while substitute_letter not in ['yes', 'no']:
            print('Please enter "yes" or "no"')
            substitute_letter = input('Would you like to substitute a letter? ')

        if substitute_letter == 'yes':
            letter = input('Which letter would you like to replace? ')
            hand = substitute_hand(hand, letter)  
            print('Current Hand: ', end=' ')
            display_hand(hands[i])
            sub_letter_bool = False      
             
    hand_score = play_hand(hand, word_list)

    if i in game_score_dict and hand_score > game_score_dict[i]: 
        game_score_dict[i] = hand_score

    else:
        game_score_dict[i] = hand_score
    


    print('----------')

    if repeat_hand_bool:
        replay_hand = input('Would you like to replay the hand? ')

        while replay_hand not in ['yes', 'no']:
            print('Please enter "yes" or "no"')
            replay_hand = input('Would you like to replay the hand? ')
        
        if replay_hand == 'yes':
            i -= 1
            repeat_hand_bool = False
            sub_letter_bool = False     
    i += 1
   
print('Total score over all hands: ', sum(game_score_dict.values()))


