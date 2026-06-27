import speech_recognition as sr
import webbrowser 
import pyttsx4
import musiclibrary
from client import ask_gemini
# this is main file
# made by manav :)
engine = pyttsx4.init()
r = sr.Recognizer()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open cricbuzz" in c.lower():
        webbrowser.open("https://cricbuzz.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        link=musiclibrary.music[song]
        webbrowser.open(link)
    else:
        #let ai handel request
        reply = ask_gemini(c)
        print(reply)
        speak(reply)


if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:
        # listen for the wake word "jarvis"
        # obtain audio from the microphone
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2 )
            word = r.recognize_google(audio)
            print(word)
            if "jarvis" in word.lower():
                speak("yes") 
                # listen for command 
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("command recived:",command)
                    processcommand(command)
            elif (word.lower()=="over"):
                speak("thank you for using me...")
                speak("made by manav")
                break
        except Exception as e:
            print("error; {0}".format(e))
