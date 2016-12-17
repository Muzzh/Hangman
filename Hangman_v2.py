

import sys
import random

def create_list(file):
    #creates the list from provided file
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
    #prepares a list containing lists of letter-clue couples
    word = working_list.pop(-1)
    letter_list = list(word)
    hangman = []
    for letter in letter_list:
        hangman.append([letter, '_ '])
    return hangman


def play(working_list):
    #mother function
    hangman = prep_hang(working_list)
    session = 0
    max_tries = 3
    letters_used = []
    while session < max_tries:
        clue = prep_clue(hangman)
        letter = get_letter(clue, (max_tries - session), letters_used)
        letters_used.append(letter)
        hangman = check_letter(hangman, letter)
        clue = prep_clue(hangman)
        session += 1
        print 'This is the letters you have found:\n{}'.format(''.join(clue))
        ready = ask_for_final_answer()
        if ready == 'yes':
            ask_solution(hangman)
        else:
            None
    ask_solution(hangman)
    restart()

def prep_clue(hangman):
    #prepares just the clue and updated clues
    clue = []
    for couple in hangman:
        clue.append(couple[1])
    return clue

def get_letter(clue, attempts, letters_used):
    #ask for a letter providing the clue and updated clue each time
    print '\nFind this word!'
    print ''.join(clue)
    used = '-'.join(letters_used)
    letter = raw_input('''Choose a letter you think might be in this hidden word\expression
    You have {} tries left
    These are the letters you've already asked for: {}
    >  '''.format(attempts, used))
    return letter

def check_letter(hangman, letter):
    #verify the letter provided and changes the associated letter if correct
    for item in hangman:
        if item[0] == letter:
            item[1] = item[0] + ' '
        else:
            None
    return hangman

def ask_for_final_answer():
    #ask user if ready to give the final answer
    final = raw_input('Are you ready to give your final answer? [Y\N]\n> ')
    if final.lower() == 'y':
        return 'yes'
    elif final.lower() == 'n':
        return 'NOT READY!!!!!!'
    else:
        print 'Please answer Y or N!'
        ask_for_final_answer()

def ask_solution(hangman):
    #checks if the final answer provided is == to the hangman
    solution = []
    for couple in hangman:
        solution.append(couple[0])
    solution = ''.join(solution)
    answer = raw_input('Can you provide the full word\expression?\n> ')
    if answer == solution:
        print 'Congratulations !! You found the word!'
    else:
        print 'NOOOO! You failed to prevent the Hangman from killing an innocent person!! :('
        print 'The correct answer was'.format(solution)

def restart():
    redo = raw_input('Another try? [Y/N]\n> ')
    if redo.lower() == 'n':
        menu = raw_input('Would you like to go back to the main menu? [Y/N]\n> ')
        if menu.lower() == 'y':
            main()
        elif menu.lower() == 'n':
            sys.exit(0)
        else:
            print 'Please answer Y or N'
            restart()
    elif redo.lower() == 'y':
        play(hangman)
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
    elif choice == 'q':
        sys.exit(0)
    else:
        None

main()
