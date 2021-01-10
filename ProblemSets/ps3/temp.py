def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')
    print()

VOWELS = 'aeoou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def deal_hand(n):
    hand = {}
    num_vowles = int(math.ceil(n/3))

    for i in range(num_vowels):
        x in random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels):
        x in random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    return hand

def update_hand(hand, word):
    new_hand = hand.copy()

    for i in word:
        if i in new_hand:
            new_hand[i] -= 1

    for key, val in dict(new_hand).items(): # USEFUL CODE
        if val <= 0:                        # Tidies up dictionary based on condition
            del new_hand[key]

    return new_hand

def get_word_score(word, n):
    word = str.lower(word)
    component1 = 0 
    for letter in word:
       component1 += SCRABBLE_LETTER_VALUES[letter] 

    word_length = len(word)
    component2 = 7*word_length - 3*(n - word_length)

    if component2 > 1:
        return component1*component2
    else:
        return component1

 def is_valid_word(word, hand, word_list):
    word_dict = {}
    for letter in word:
        letter = str.lower(letter)
        if letter not in word_dict:
            word_dict[letter] = 1
        else:
            word_dict[letter] += 1    
        
    valid_number_letters = True

    for key in word_dict:
        if key not in hand:
            return False
        elif hand[key] < word_dict[key]:
            valid_number_letters = False

    if word not in word_list and not valid_number_letters:
        return False
    else:
        return True



hand = {"c" : 1, "o" : 1, "w" : 1, "s" : 1 , "*" : 1, "z" : 1}
