from nltk.corpus import wordnet
import sys
from gtts import gTTS
import os
search = input('Enter the result to search: ')
# setting setence
out_come = wordnet.synsets(search)
# print data
print(out_come)
'''
def exception_handler(exception_type, exception, traceback):
        # All your trace are belong to us!
        # your format
     print() # to track the error u can put ("%s: %s" % (exception_type.__name__, exception)) inside print
sys.excepthook = exception_handler
'''
# definition
language='en'
sp=out_come[0].definition()
print("\n 1. noun: ", sp)
print('Expamples: ', out_come[0].examples())

print('\n 2. adg:  ', out_come[1].definition())
print('Expamples: ', out_come[1].examples())

print('\n 3. adv:  ', out_come[2].definition())
print('Expamples: ', out_come[2].examples())

myobj=gTTS(text=sp,lang=language,slow=False)
myobj.save('word.mp3')
os.system("mpg123 --play-and-exit word.mp3")
os.remove('word.mp3')
