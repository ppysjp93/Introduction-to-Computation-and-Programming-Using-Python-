# coding: utf-8
import random
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
ALPHABET = VOWELS + CONSONANTS

def substitute_hand(hand, letter):

    set_hand_keys = set(tuple(hand.keys()))

    if letter in set_hand_keys:

        set_alpha = set(ALPHABET) # Technically constant, start of script
        alpha_hand_keys = set_alpha - set_hand_keys

        new_letter = random.choice(tuple(alpha_hand_keys))
        hand[new_letter] = hand.pop(letter)

    return hand

hand = {'h':1, 'e':1, 'l':2, 'o':1}
letter = 'l'
new_hand = substitute_hand(hand, letter)

print("\nnew_hand = ", str(new_hand))

hand = {'h':1, 'e':1, 'l':2, 'o':1}
letter = 'r'
new_hand = substitute_hand(hand, letter)

print("\nnew_hand = ", str(new_hand))
