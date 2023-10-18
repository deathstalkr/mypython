from gtts import gTTS
import os
#import sys
mytext= "Hi how are you"

language= "en"
#def exception_handler(exception_type, exception, traceback):
    #print()
    #sys.excepthook = exception_handler
a=2
myobj=gTTS(text=mytext, lang=language,slow=False)
myobj.save("speech.mp3")
for i in range(a):
    i+=1;
    os.system("mpg321 speech.mp3")
