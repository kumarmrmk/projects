import pyttsx3
import os 
import time
import speech_recognition as sr
import pyaudio

def listening():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("listening.....")
        audio=r.listen(source)
    try:
        voice=r.recognize_google(audio, language=' en-in')
        print(f"you said {voice}.")
    except:
        print("sorry I cant recognize...")
        pyttsx3.speak("sorry I cant recognize..., can you say that again")
        return 'None'
    return voice
        

pyttsx3.speak("hi BOSS")
while True:
    print("what can i do for u:",end="")
    #time.sleep(1)
    print()
    pyttsx3.speak("what can i do for u: ")

    p=listening().lower()
    
    if "don't" in p and ("chrome" in p or "notepad" in p or "player" in p or "editor" in p):
        pyttsx3.speak("ok then iam not running ")
    elif ("run" in p or "open" in p) and "chrome" in p:
        os.system("chrome")
    elif "run" in p or "open" in p and "notepad" in p:
        os.system("notepad")
    elif "run" in p or 'open' in p and "player" in p or "media" in p:
        os.system("wmplayer")
    elif "run" in p or "open" in p and "telegram" in p:
        os.system("telegram")
    elif "bye" in p or "quit" in p or "exit" in p or "see u later" in p or "nothing" in p:
        pyttsx3.speak("ok byee,       see u later.")
        break
    else:
        pyttsx3.speak("check your internet conection and try again")





        # in process
	 
