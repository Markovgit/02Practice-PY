import pyttsx3 # install using pip install pyttsx3 
import datetime 
import speech_recognition as sr 
import wikipedia
#import webbrowser 
import webbrowser as wb
import smtplib
import os
import pyautogui






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
    
        
    speak(" Im Jarvis , an AI assistant. tell me how can I help you sir")

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


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('tvoj mejl','password here')###################################################
    server.sendmail('Your email',kome,sadrzaj) # wtite to whome in "kome" section and what are you sending in "sadrzaj" section
    server.close()


def system_info():
    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    speak("CPU usage is {} percent".format(cpu_usage))

    # Memory usage
    memory = psutil.virtual_memory()
    speak("Memory usage is {:.2f} gigabytes".format(memory.used / (1024**3)))

    # Disk usage
    disk = psutil.disk_usage('/')
    speak("Disk usage is {:.2f} percent".format(disk.percent))





#takeCommand()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()  

        elif "wikipedia" in query:
            speak("Searching..")   
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 2 )  
            print(result)
            speak(result)

         

        elif 'send email' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = 'sample@email.com'############################## write the email address to whom you are sending the email
                sendEmail(to,content)
                speak("Email is been sent ")
            except Exception as e:
                    speak("Unable to send the email")



        elif 'search in chrome' in query:
            speak("What should I search") 
            chromepath ='C:/Program Files/Google/Chrome/Application/chrome.exe'   
            search = takeCommand().lower()     
            wb.get(chromepath).open_new_tab(search+'.com')   

        elif 'logout' in query:
            os.system("shutdown -1")      

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")    

        elif 'restart' in query:
            os.system("shutdown /r /t 1")      


        elif 'play songs' in query:
            songs_dir = 'D:\\muzika'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'remember that' in query:
            speak("what should I remember sir")
            data = takeCommand()
            speak("you said me to remember"+ data)
            remember = open('data.text','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you said to me to remember"+ remember.read())


        elif 'screenshot' in query:
            speak("Taking screenshot")
            # Take screenshot and save it to a file
            pyautogui.screenshot('screenshot.png')
            speak("Screenshot taken successfully")

        elif 'system info' in query:
            speak("Gathering system information")
            system_info()

        




        
        elif 'offline' in query:
            quit()



    



