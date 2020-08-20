import pyttsx3
import os 
import time

pyttsx3.speak("hi BOSS")
while True:
    print("what can i do for u:",end="")
    #time.sleep(1)
    print()
    pyttsx3.speak("what can i do for u: ")

    p=input()
    
    if "dont" in p and ("chrome" in p or "notepad" in p or "player" in p or "editor" in p):
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
        pyttsx3.speak("sorry something went wrong, try again")
	 
