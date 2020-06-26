import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


#Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis:listening...")
        audio = r.listen(source)
        
    try:
        query = r.recognize_google(audio,language="en-in")
        print(query)
        
    except Exception as e:
        print("speak that again please..{0}".format(e))
        query= takecommand()

    return query