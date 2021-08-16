def print_upper_words(word_list):
    ''' prints upper cased version of all words in a list'''
    for word in word_list:
        print(f'{word.upper()}')

def print_ewords(word_list):
    ''' Prints all words in a list that start with "e" or "E" '''
    for word in word_list:
        if word.startswith('e') or word.startswith('E'):
            print(word)

def print_correct_words(word_list, must_start_with):
    """ Prints all words that start with the given letter regardless of case"""           
    for word in word_list:
        if word[0] in must_start_with:
            print(f'{word.upper()}')
