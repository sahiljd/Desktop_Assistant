import speech_recognition as sr
import wikipedia
import datetime
import os
import webbrowser
import random
import pyttsx3


def speak(text):
    
     engine = pyttsx3.init()
     engine.setProperty('voice','HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
     engine.setProperty('volume',1.0)
     print(text)
     engine.say(text)
     engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\nListening...')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print('Recognizing...')
            said = r.recognize_google(audio)
            print(said)
            return said
        except sr.UnknownValueError:
            speak('Sorry, I couldn\'t understand what you said.')
        except sr.RequestError:
            speak('Sorry, I encountered an error while processing your request.')

    return None


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon ')
    else:
        speak('Good Evening ')

    speak("Hi I'm Sarah, Sahil's Assistant. How may I help you??")


if __name__ == "__main__":
    wishMe()
    while True:
        query = get_audio().lower()
        if 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            newquery = query.replace('wikipedia', "")
            results = wikipedia.summary(newquery, sentences=2)
            speak(results)

        elif 'create a folder' in query:
            speak('Tell the name of the folder you wanna create')
            name_folder=get_audio()
            speak('Creating a Folder named '+name_folder)
            os.mkdir(name_folder)

        elif 'time' in query:
            hours = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute)
            sec = int(datetime.datetime.now().second)
            speak('The time is '+str(hours)+' hours ' +
                  str(min)+' minutes '+str(sec)+' seconds')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\sahil\\Desktop\\musics"
            speak('You have the following songs in your Folder')
            os.chdir(music_dir)
            music_list = os.listdir(music_dir)
            print(music_list)
            os.startfile(random.choice(music_list))
            
        elif 'who are you' in query:
            speak("As i mentioned your earlier I'm Sarah, Sahil's Assistant.")
        
        elif 'current directory' in query:
            speak(os.getcwd())
        
        elif 'change directory' in query:
            speak('Please type the directory you wanna go to')
            new_dir=input()
            os.chdir(new_dir)
            speak('Your in the new directory')
                    
        elif 'exit' in query or 'thank you' in query:
            speak('I hope i helped you!!')
            break    
