word = 'Rapture'
word_dict = {}
for letter in word:
    letter = str.lower(letter)
    if letter not in word_dict:
        word_dict[letter] = 1
    else:
        word_dict[letter] += 1    
    
hand = {'r':1, 'a':3, 'p':2, 'e': 1, 't': 1, 'u': 1}
valid_number_letters = True
for key in word_dict:
    if key not in hand or hand[key] < word_dict[key]:
        valid_number_letters = False

assert(valid_number_letters == False)

word = 'honey'
word_dict = {}
for letter in word:
    letter = str.lower(letter)
    if letter not in word_dict:
        word_dict[letter] = 1
    else:
        word_dict[letter] += 1    
    
hand = {'r':1, 'a':3, 'p':2, 't': 1, 'u': 1}
valid_number_letters = True

for key in word_dict:
    print(key not in hand)
