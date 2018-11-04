import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

dataFile = json.load(open('c://users//trent//desktop//data.json'))

def definedWord(aWord):
    if aWord in dataFile:
        return dataFile[aWord]
    else:
        return 'The word doesn\'t exist. Did you mean ', get_close_matches(aWord, dataFile.keys(), cutoff=0.5)[0], '.' 

enteredWord = input('Enter a word: ')
enteredWord = enteredWord.lower()

print(definedWord(enteredWord))
