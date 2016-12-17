

import sys
import random

def create_list(file):
    pulled_list = []
    with open(file) as f:
        lines = f.read().split('\n')
        random.shuffle(lines)
        for line in lines:
            if len(line) >= 8:
                pulled_list.append(line)
            else:
                None
    working_list = []
    max_lenght_of_word_list = 500
    while len(working_list) <= max_lenght_of_word_list:
        working_list.append(pulled_list.pop(-1))
    return working_list

def prep_hang(working_list):
    word = working_list.pop(-1)
    print word
    letter_list = list(word)
    hang_dict = []
    for letter in letter_list:
        hang_dict.append([letter, '_ '])
    return hang_dict

#def play(list):
#    hangman =

def get_letter():
    letter = raw_input('Choose a letter you think might be in this hidden word\expression\n> ')
    return letter

def check_letter():
    hangman = prep_hang()
    print hangman
    session = 0
    clue = []
    for couple in hangman:
        clue.append(couple[1])
    print '\nFind this word!'
    print ''.join(clue)
    while session <= 4:
        session += 1
        print 'You have {} attempts left !'.format((6 - session))
        letter = get_letter()
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

def verify_answer():
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
        1. Words
        q. Leave the game :(
        >''')
    if choice == '1':
        word_list = create_list('englishwords.txt')
        hangman = prep_hang(word_list)

        print hangman
#        verify()
    elif choice == 'q':
        sys.exit(0)
    else:
        None

main()
