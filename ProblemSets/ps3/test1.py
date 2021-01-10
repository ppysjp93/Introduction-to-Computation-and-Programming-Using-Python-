word = 'Rapture'
hand = {'r':1, 'a':3, 'p':2, 'e': 1, 't': 1, 'u': 1}

word = 'honey'
hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u': 2}

word_dict = {}
for letter in word:
    letter = str.lower(letter)
    if letter not in word_dict:
        word_dict[letter] = 1
    else:
        word_dict[letter] += 1    
    
valid_number_letters = True

for key in word_dict:
     a = key not in hand
     print("key not in hand = ", str(a))
     if key not in hand or hand[key] < word_dict[key]:
         valid_number_letters = False
     print("valid_number_letters = ", str(valid_number_letters))

