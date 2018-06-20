import speech_recognition as sr
r = sr.Recognizer()

jackhammer = sr.AudioFile("jackhammer.wav")
with jackhammer as source:
    r.adjust_for_ambient_noise(source,duration=0.5)
    audio = r.record(source)
out=r.recognize_sphinx(audio,show_all=True)
print(out)
