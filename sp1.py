import speech_recognition as sr
r = sr.Recognizer()

jackhammer = sr.AudioFile("jackhammer.wav")    #jachammer.wav is an audio file with background noise of jackhmmer
with jackhammer as source:
    r.adjust_for_ambient_noise(source,duration=0.5)  #it removes unwanted noise.....duration is set to 1 by default
    audio = r.record(source)
out=r.recognize_google(audio,show_all=True)  #in place of google u cwn replace it with other suppotred API's
print(out)
