import speech_recognition as sr
r = sr.Recognizer()

harvard = sr.AudioFile("harvard.wav")     #you can download the audio file from this same repository
with harvard as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
out=r.recognize_google(audio)
print(out)
