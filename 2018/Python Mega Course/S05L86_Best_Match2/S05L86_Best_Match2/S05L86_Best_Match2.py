import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

dataFile = json.load(open('c://users//trent//desktop//data.json'))

def definedWord(aWord):
    if aWord in dataFile:
        return dataFile[aWord]
    elif len(get_close_matches(aWord, dataFile.keys())) > 0:
        ynAnswer = input('Did you mean %s instead? Enter y if Yes, or n if No. ' %get_close_matches(aWord, dataFile.keys(), cutoff=0.5)[0])
        ynAnswer = ynAnswer.lower()
        if ynAnswer == 'y':
            return dataFile[get_close_matches(aWord, dataFile.keys())[0]]
        elif ynAnswer == 'n':
            return 'The word doesn\'t exist. Please double check it.'
        else:
            return 'We didn\'t understand your query.'
    else:
        return 'The word doesn\'t exist. Please try again.' 

enteredWord = input('Enter a word: ')
enteredWord = enteredWord.lower()


print(definedWord(enteredWord))

