import json
from difflib import get_close_matches
word_list = json.load(open('dictionary.json'))


def Meaning(word):
    word=word.lower()
    if word in word_list.keys():
        print('Searched meaning of word : ', word)
        return word_list[word]
    elif word.title() in word_list.keys():
        print('Searched meaning of word : ', word.title())
        return word_list[word.title()]
    elif word.upper() in word_list.keys():
        print('Searched meaning of word : ', word.upper())
        return word_list[word.upper()]
    elif word.capitalize() in word_list.keys():
        print('Searched meaning of word : ', word.capitalize())
        return word_list[word.capitalize()]
    elif get_close_matches(word, word_list.keys()):
        print('Searched meaning of word : ', get_close_matches(word, word_list.keys())[0])
        return word_list[get_close_matches(word, word_list.keys())[0]]
    else:
        return 'No such word exists'



cont = True
while(cont):
    word = input('Enter a word : ')
    mean = Meaning(word)
    print(mean)
    print('________________________________________')
    v = input('Do you want to continue?(y/n) : ')
    if v == 'n':
        cont = False
        print('EXITING...')