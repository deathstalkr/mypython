import speech_recognition as sr
#from gtts import gTTS
#import os
import pyaudio

# get audio from the microphone
output=0
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something:")
        audio = r.listen(source)

    try:
        output=r.recognize_google(audio,language='en')
        print(output)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results.Please check your internet connection and try again; {0}".format(e))

    if output=='close':
        break
    else:
        continue
