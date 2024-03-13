import pyttsx3 # install using pip install pyttsx3 
import datetime 
import speech_recognition as sr 





engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is :")
    speak(Time)


def date():
    day = int (datetime.datetime.now().day)
    month = int (datetime.datetime.now().month)
    year = int (datetime.datetime.now().year)
    speak("the current date is :")

    

    speak(day)
    speak(month)
    speak(year)
    
    
def wishme():
    speak("welcome back sir")
    
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("good morning sir , have a cup of cafe and have a nice day")
    elif hour >=12 and hour<18:
        speak("good afternoon sir") 
    elif hour >= 18 and hour <24:
        speak("good evening sir")     
    else:
        speak("good night sir")
    
        
    speak("for now that is that is all I can tell you sir, Im Jarvis , an AI assistant")

#wishme()
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google( audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again Sir")


        return "None"

    return query

#takeCommand()

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()    
        
        elif 'offline' in query:
            quit()



    



