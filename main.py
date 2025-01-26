# pip install pyaudio

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime #ye hmaara built in module hota h, np need to install it ...used to find date &time
import wikipedia #pip install wikipedia
import webbrowser
import os
import sys
import smtplib   #which uses SMTP protocols and help to send email through gmail

engine = pyttsx3.init('sapi5') #sapi5 ek API h jisse hm windows me inbuilt voices ko use kr skte h
voices = engine.getProperty('voices')  #voices ko pickup krne ke liye
# print(voices[1].id)    #aur agr hm voices[1].id lete h to isme ZIRA name ki female ki voice h
engine.setProperty('voice', voices[0].id)  # voices[0].id pr hmaari male (David) ki voice h


def speak(audio):    #iss func ki help se hmaari AI bol payegi
    engine.say(audio)   #isme hm diff-diff chize bulvayeinge hmaare program me
    engine.runAndWait()   #as the name clears


def wishMe():                        #ki hmaara jarvis kuch help krne se phke hme wish krega
    hour = int(datetime.datetime.now().hour)   #func to find time so that it can wish acc. to that
                                                #0-24 tk ke hour mil jaayenge
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you") #wish krne ke baad jarvis apne baare me btayegas   

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()  #ye jo hmaari recognizer class h ye hme audio ko detect krne me help kregi
                          #iske andr hmaare bhut saare func h jise hm ctrl+tab press krke dekh skte h
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   # pause_threshold~~seconds of non speaking audio before a phrase 
                                 #is considered complete....here =1 shows mtlb it wait for 1 sec
        audio = r.listen(source)

    try:                                 #mtlb yha hmaare error generte hone ke chances h
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') # here en-in = english india
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aarti163431@gmail.com', 'your-password')
    server.sendmail('aarti163431email@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)  #mtlb ye wikipdeia se 2 sentences uthayega...hm iski value change bhi kr skte h
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  #webbrowser hmaara ek inbuilt package hota h , jo hme yha youtube open krke dega

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'open linkedin' in query:
            codePath="https://www.linkedin.com/feed/" 
            os.startfile(codePath)


        elif 'play music' in query:
            music_dir = "C:/Users/ASUS/Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))   #it plays the first song in directory

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
 
        elif 'open code' in query:             #hm yha koi particular program bhi open krva skte h
            codePath = "D://downloads//Microsoft VS Code//Code.exe"
            os.startfile(codePath)

        elif 'email to aarti' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "aarti163431@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend 😅. I am not able to send this email")    
                
        # New functionality to quit the program
        elif 'quit' in query:
            speak("Jarvis shutting down. Goodbye, Sir!")
            break  # Exit the program
    
        else:
            print("No query matched")