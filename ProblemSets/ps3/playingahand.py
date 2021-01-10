
def play_hand(hand, word_list):

    handlen = -1
    total_score = 0
    
    while handlen != 0:
        display_hand(hand)
        handlen = calculate_handlen(hand)
        word = input('Enter a word, or "!!" to indicate that you are finished: ')
        end_of_game = word == '!!'

        if end_of_game:
            break

        hand = update_hand(hand, word)
        
        if not is_valid_word(word, hand, word_list): 
            print('That is not a valid word. Please choose another word.')
            continue

        word_score = get_word_score(word, handlen)
        total_score += word_score
        
        print('"{0}" earned {1} points. Total score: {2} points'.format(word, \
                word_score, total_score))
         
    print('Ran out of letters. Total score: {0} points'.format(total_score))
        


