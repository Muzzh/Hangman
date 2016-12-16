

import sys
import random

def get_word():
    words = []
    pulled_list = []
    with open('englishwords.txt') as f:
        lines = f.read().split('\n')
        random.shuffle(lines)
        for line in lines:
            if len(line) >= 8:
                pulled_list.append(line)
            else:
                None
    while len(words) <= 15:
        words.append(pulled_list.pop(-1))
    return words.pop(-1)

def prep_hang():
    word = get_word()
    word_list = list(word)
    hang_dict = []
    for letter in word_list:
        hang_dict.append([letter, '_ '])
    return hang_dict

def get_letter():
    letter = raw_input('Choose a letter you think might be in this hidden word\expression\n> ')
    return letter

def check_letter():
    hangman = prep_hang()
    session = 0
    clue = []
    tried_letters = []
    for couple in hangman:
        clue.append(couple[1])
    print '\nFind this word!'
    print ''.join(clue)
    while session <= 4:
        session += 1
        print 'You have {} attempts left !'.format((6 - session))
        if len(tried_letters) > 0:
            print 'So far, you have tried these letters: {}'.format('-'.join(tried_letters))
        else:
            None
        letter = get_letter()
        tried_letters.append(letter)
        for item in hangman:
            if item[0] == letter:
                item[1] = item[0] + ' '
            else:
                None
        clue = []
        for couple in hangman:
            clue.append(couple[1])
        print '\nFind this word!'
        print ''.join(clue)

    return hangman

def verify():
    hangman = check_letter()
    solution = []
    for couple in hangman:
        solution.append(couple[0])
    solution = ''.join(solution)
    answer = raw_input('Can you provide the full word\expression?\n> ')
    if answer == solution:
        print 'Congratulations !! You found the word!'
    else:
        print 'NOOOO! You failed to prevent the Hangman from killing an innocent person!! :('
        print 'The answer was: {}'.format(solution)
    redo = raw_input('Another try ?\n[Y/N]> ')
    if redo.lower() == 'n':
        sys.exit(0)
    elif redo.lower() == 'y':
        main()
    else:
        None

def main():
    choice = raw_input('''
        Welcome to Basic Hangman!
        Select a category:
        1. words
        q. Leave the game :(
        >''')
    if choice == '1':
        verify()
    elif choice == 'q':
        sys.exit(0)
    else:
        None

main()
