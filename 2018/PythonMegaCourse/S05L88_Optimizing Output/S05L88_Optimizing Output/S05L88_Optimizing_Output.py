import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

dataFile = json.load(open('d://users//trent//desktop//data.json'))

def giveDefinition(aWord):
    if aWord in dataFile:
        return dataFile[aWord]
    elif len(get_close_matches(aWord, dataFile.keys())) > 0:
        ynAnswer = input('Did you mean %s instead? Enter Y if yes, or N if no: ' %get_close_matches(aWord, dataFile.keys())[0])
        ynAnswer = ynAnswer.lower()
        if ynAnswer == 'y':
            return dataFile[get_close_matches(aWord, dataFile.keys())[0]]
        elif ynAnswer == 'n':
            return 'The word doesn\'t exist. Please double check it.'
        else:
            return 'We didn\'t understand your entry.'
    else: 
        return 'The word doesn\'t exist. Please double check it.'
    
userWord = input('Enter word: ')
userWord = userWord.lower()

stringOutput = giveDefinition(userWord)

if type(stringOutput) == list:
    for listItem in stringOutput:
        print(listItem)

else:
    print(stringOutput)

