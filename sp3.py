import speech_recognition as sr
import pyaudio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
try:
    print("You said" + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("error; {0}".format(e))
