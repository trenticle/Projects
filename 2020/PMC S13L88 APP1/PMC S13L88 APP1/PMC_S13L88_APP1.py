import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


data = json.load(open('d:\\Users\\trent\\Desktop\\Sandbox\\data2.json'))

def translate(word):
    word = word.lower
    if word in data:
        return data[word]
    else:
        return "the word doesn't exist"

word = input('Enter word: ')

print(translate(word))
