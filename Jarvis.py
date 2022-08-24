import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voice')
engine.setProperty('voice', voice[1].isidentifier)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning!!")    

    elif hour >= 12 and hour<18:
        speak("Good Afternon!!")

    else:
        speak("Good Evening!!")

    speak("I am Jarvis. Sir, Please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)  

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  


    except Exception as e:
        # print(e)

        print("Say that again please.....") 
        return "None" 
    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

    
    # Logic for executing tasks bassed on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        speak("According to wikipedia....")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")  

    elif 'open github' in query:
        webbrowser.open("github.com") 

    elif 'play music' in query:
        music_dir = 'D:\\music' 
        songs = os.listdir(music_dir)
        print(songs)  
        os.startfile(os.path.join(music_dir, songs[0]))    

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir, the time is {strTime}") 

    elif 'open code' in query:
        codePath = "C:\\Users\\srijib ghosh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"       
        os.startfile(codePath)   

    elif 'open whatsapp' in query:
        path = "C:\\Users\\srijib ghosh\\AppData\\Local\\WhatsApp\\WhatsApp.exe"   
        os.startfile(path)   

         

    elif 'email to someone' in query:
        try:
            speak("What shoud i say?")
            content = takeCommand()
            to = "someone@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!!")
        except Exception as e:
            print(e)
            speak("Sorry my friend srijib. I am not able to send this email at the moment")   
