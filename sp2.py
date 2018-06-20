import speech_recognition as sr
import pyaudio   #optional

# get audio from the microphone
while True:                     #this loop runs the below code infinite times until any inturrupt is generated 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Speak:")
        audio = r.listen(source)

    try:
        output= r.recognize_google(audio,language='en')  #can change language to your desired language 
        print("You said: " +output)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results.Please check your internet connection and try again; {0}".format(e))
    if output=='exit':     #if the input voice is matched with the passed argument the loop terminates 
        break
    else:                  #loop continues to run
        continue
