from ctypes.wintypes import LPWORD
from sys import flags, float_repr_style
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser, os, smtplib, datetime, random

from wikipedia.wikipedia import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def lightSystem(status): 
    import serial
    import time

    arduino=serial.Serial('COM3', 9600) #Change the COM port to where the arduino is connected
    time.sleep(2)
    datafromUser=''
    if 'on' in status:
        datafromUser='1'
    elif 'off' in status:
        datafromUser = '0'
    else:
        return
    
    if datafromUser == '1':
        arduino.write(b'1')
        speak('Lights were truned on')
        return
    elif datafromUser == '0':
        arduino.write(b'0')
        speak('Lights were truned off')
        return
def search_internet(query):
    querys = {"google":"https://www.google.com/search?q=",
    "youtube":"https://www.youtube.com/results?search_query="}
    if 'youtube' in query:
        newLink = querys['youtube']+((str(query).replace('youtube','')).replace(' ','+'))
        webbrowser.open_new(newLink)
    else:
        newLink = querys['google']+((str(query).replace('google','')).replace(' ','+'))
        webbrowser.open_new(newLink)


def manageTaske(query):
    query = str(query).replace('jarvis','')
    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak ('opening youtube')
        webbrowser.open_new('https://www.youtube.com')
    
    elif 'open whatsapp' in query:
        speak ('opening Whatsapp Web')
        webbrowser.open_new('https://web.whatsapp.com/')
    
    elif 'join class' in query:
        speak ('Joinig 9 B now')
        webbrowser.open_new('https://dpsbaes.webex.com/meet/class9b')
    
    elif 'open google' in query:
        speak ('opening google')
        webbrowser.open_new('https://www.google.com')   

    elif 'play' and 'music' in query:
        speak ('Here you Go sir... i hope you like this')
        music_dir = 'C:\\Users\\Harsh\\Desktop\\Disraction\\Music'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs)-1)]))

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")

    elif 'coding' in query:
        speak('ok sir, i am opening Visual Studio Code')
        codePath = "C:\\Users\\Harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    
    elif 'spotify' in query:
        codePath = "C:\\Users\\Harsh\\AppData\\\\Roaming\\Spotify\\Spotify.exe"
        os.startfile(codePath)

    elif 'lights' in query:
        lightSystem(query)

    elif 'light' in query:
        lightSystem(query)
    
    elif 'stop' in query:
        speak('Ok Sir, Jarvis Signing Off')
        exit()
    elif 'search in' in query:
        search_internet(str(query).replace('search in',''))
    else:
        pass

if __name__ == "__main__":
    wishMe()
    while True:
        manageTaske(takeCommand().lower())
