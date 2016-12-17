

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
    hangman = []
    for letter in letter_list:
        hangman.append([letter, '_ '])
    return hangman

def prep_clue(hangman):
    clue = []
    for couple in hangman:
        clue.append(couple[1])
    return clue


def play(working_list):
    hangman = prep_hang(working_list)
    print hangman
    session = 0
    max_tries = 3
    while session < max_tries:
        clue = prep_clue(hangman)
        letter = get_letter(clue, (max_tries - session))
        new_hangman = check_letter(hangman, letter)
        clue = prep_clue(new_hangman)
        session += 1


def get_letter(clue, attempts):
    print '\nFind this word!'
    print ''.join(clue)
    letter = raw_input('''Choose a letter you think might be in this hidden word\expression
    You have {} tries left
    >  '''.format(attempts))
    return letter

def check_letter(hangman, letter):
    for item in hangman:
        if item[0] == letter:
            item[1] = item[0] + ' '
        else:
            None
    #clue = []
    #for couple in hangman:
    #    clue.append(couple[1])
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
        play()
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
        working_list = create_list('englishwords.txt')
        play(working_list)
#        verify()
    elif choice == 'q':
        sys.exit(0)
    else:
        None

main()
