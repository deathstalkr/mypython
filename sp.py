import speech_recognition as sr
r = sr.Recognizer()

harvard = sr.AudioFile("harvard.wav")
with harvard as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
out=r.recognize_sphinx(audio)
print(out)
