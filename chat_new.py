from nltk.corpus import wordnet
import sys
from gtts import gTTS
import os
import speech_recognition as sr
output=0
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something:")
        audio = r.listen(source)

    try:
        output=r.recognize_google(audio,language='en')
        print("You said: " + output)
    except sr.UnknownValueError:
        print("Could not understand audio")
        continue
    except sr.RequestError as e:
        print("Could not request results.Please check your internet connection and try again; {0}".format(e))
        continue
    if output=='close':
        break
    else:
        out_come = wordnet.synsets(output)
        # print data
        #print(out_come)

        def exception_handler(exception_type, exception, traceback):
                # All your trace are belong to us!
                # your format
            print() # to track the error u can put ("%s: %s" % (exception_type.__name__, exception)) inside print
        sys.excepthook = exception_handler

        # definition
        language='en'
        sp=out_come[0].definition()
        '''
        print("\n 1. noun: ", sp)
        print('Expamples: ', out_come[0].examples())

        print('\n 2. adg:  ', out_come[1].definition())
        print('Expamples: ', out_come[1].examples())

        print('\n 3. adv:  ', out_come[2].definition())
        print('Expamples: ', out_come[2].examples())
        '''
        myobj=gTTS(text=sp,lang=language,slow=False)
        myobj.save('word.mp3')
        os.system("cvlc --play-and-exit word.mp3")
        os.remove('word.mp3')
