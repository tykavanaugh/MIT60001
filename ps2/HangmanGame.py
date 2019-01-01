'''
Python based hangman game for the MIT open course
'''

import random
import sys


def is_word_guesssed(secret_word,letters_guessed):
    '''
    Returns boolean values to determine if game should continue
    '''
    guess = True
    for i in secret_word:
        if i not in letters_guessed:
            guess = False
    return guess

def get_guessed_word(secret_word,letters_guessed):
    '''
    Prints out of blanked version of secret word for unguessed letters
    '''
    output = []
    for i in secret_word:
            if i in letters_guessed:
                output.append(i)
            else:
                output.append('_')
    output = ''.join(output)
    return(output)
    
def get_available_letters(letters_guessed,alphabet):
    '''
    updates a list of unguessed letters
    '''
    for i in letters_guessed:
        if i in alphabet:
            alphabet = alphabet.replace(i,'')
    return alphabet




WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish. (Function provided by professor)
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random (Function provided by professor)
    """
    return random.choice(wordlist)



def hangman(maxWarnings):
    '''
    Hangman game
    '''
    permalphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    letters_guessed = []
    warnings = 0
    while not is_word_guesssed(secret_word,letters_guessed):
        print('You have {} warnings of {}'.format(warnings,maxWarnings))
        print(get_guessed_word(secret_word,letters_guessed))
        print('You have these letters still to choose from:')
        print(get_available_letters(letters_guessed,alphabet))
        print('Type * for hints')
        guess = input('Please type a lowercase letter you would like to guess\n')
        if guess == '*':
            print(hint(letters_guessed,wordlist,secret_word))
        guess = guess.lower()
        if len(guess) != 1:
            print('\nPlease only type one character\n')
        elif guess not in permalphabet:
            print('\nPlease only type a letter\n')
        elif guess not in letters_guessed:
            print('\nYou guessed {}\n'.format(guess))
            if guess in secret_word:
                print('Good guess!')
            else:
                print('You missed!')
                warnings += 1
                if warnings == maxWarnings:
                    print('Oh no! You lose')
                    print('The word was {}'.format(secret_word))
                    return False
                    menu()
            letters_guessed.append(guess)
        else:
            print('You already guessed {}\n'.format(guess))
        print('------------------------------')
    print('The word is {}\n'.format(secret_word))
    print('Congrats! You win!')
    return (True)
    menu()


def menu(maxWarnings = 5):
    print('Hello! Welcome to hangman. Actual hanging man coming "soon"!' )
    userInput = input('Type "hangman" to play hangman.\nType "options" to change options\nType "random word" to get a random word without starting a game.\nType "exit" to exit\n')
    userInput = userInput.lower()
    if userInput == 'hangman':
        hangman(maxWarnings)
    if userInput == 'options':
        print('Options:\n-------\n1:Warnings before game ends {}'.format(maxWarnings))
        print('Type the number to select option. Typing anything else will return you to the menu')
        option = input('Please type option you would like to change here')
        if option == '1':
            option1 = input('Please choose how many warnings before game ends')
            if type(option1) != int:
                "Input error detected"
            maxWarnings = option1
    if userInput == 'random word':
        wordlist = load_words()
        word = choose_word(wordlist)
        print('')
        print(word)
        print('')
    if userInput == 'exit':
        sys.exit()
    menu(maxWarnings)

def hint(letters_guessed,wordlist,secret_word):
    properLength = []
    hint = []
    wrongLetters = []
    for word in wordlist:
        if (len(word) == len(secret_word)):
            properLength.append(word)
    for l in letters_guessed:
        if l not in secret_word:
            wrongLetters.append(l)
    for l in wrongLetters:
        for word in properLength:
            if l not in word:
                hint.append(word)
    rightLetters = []
    for i in letters_guessed:
        for l in secret_word:
            if (i == l):
                rightLetters.append(i)
    output = []
    for l in rightLetters:
        for word in hint:
            if l in word:
                output.append(word)
    return(output)
        
    

menu()