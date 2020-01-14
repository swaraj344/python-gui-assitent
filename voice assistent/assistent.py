import pyttsx3
import speech_recognition as sr
import os
import datetime
import wikipedia
from webbrowser import open
import random
import socket


def Isconnect():
    try:
        socket.create_connection(("www.google.com",80))
        return True
    except OSError:
        pass
    return False



engine= pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)
engine.setProperty('volume',1)
assistent_name=""
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wiseme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: 
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am poppy!! your persional assistent!!. please tell me  How May I help you !")

def takecommand(): # it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8       
        audio = r.listen(source)

    try:
        print("Recognizing....")
        Isinternet=Isconnect()
        if(Isinternet):
           query=r.recognize_google(audio,language="en-IN")
        else:
            query=r.recognize_sphinx(audio,language="en-US")        
        print(f"You Said : {query}\n")
    except Exception as e:
        print(e)
        print("say that again please...")
        speak("say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    # wiseme()
    count=0
    while True:
        
        query=takecommand().lower()
        
        
        
        # Logic for executing tsks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'search'in query:
            speak('searching google')
            query = query.replace("google","")
            query = query.replace("search","")
            url=f"https://www.google.com/search?hl=%(en-in)s&q={query}"
            open(url)
        elif 'play music' in query:
            speak("Playing a random music for you!!")
            music_dir = 'D:\\Music'
            songs= os.listdir(music_dir)
            song=random.choice(songs)
            print(song)
            os.startfile(os.path.join(music_dir,song))
            break
        elif 'who are you' in query:
            speak("Abbee!! saale start main hi to intro diya tha")
        elif 'chrome' in query:
            speak("starting google chrome")
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            break
        elif 'code' in query:
            speak("Starting visual studio code !!")
            os.startfile("C:\\Users\\Swaraj Kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            break
        elif 'stop' in query:
            speak("Thankyou for using my services. Bye bye!")
            speak("I Hate you!")
            break
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the Time is {strTime}")
        
        else:
            if count==3:
                speak("you mother, father Manners! thisss!!!!!.")
                break
            speak("say it again!!")
            count=count+1
            speak(query)


    
    