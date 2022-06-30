import speech_recognition as sr
r = sr.Recognizer()

#jackhammer = sr.AudioFile("jackhammer.wav")
i=10
while i>0:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    out=r.recognize_google(audio,language='en')
    print(out)
    i=i-1
