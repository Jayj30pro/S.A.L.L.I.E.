from tkinter import *
import time
import pyttsx3
import speech_recognition
from PIL import ImageTk, Image

speechSpeed = 170

def speak(phrase):
    speech = pyttsx3.init()
    speech.setProperty('rate', speechSpeed)
    speech.setProperty('voice', 'english+f4')
    speech.say(phrase)
    speech.runAndWait()



def listen(currentClient):
    recognizer = speech_recognition.Recognizer()
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            speak("Go ahead I'm listening")
            print('ready')
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()

            if currentClient == "List":
                writeToList(text)

            print(f"You said {text}") #test line
            #processSpeech(text)
    except:
        speak("I did not get that")



def processSpeech(spokenWords):
    if "note" in spokenWords:
        speak("Could you please buy me a note pad?")


    elif "list" in spokenWords:
        makeList()


def makeList():
    speak("What is the first item on the list?")
    listen("List")


def writeToList(text):
    print("it has been noted")


speak("Hi, I'm sallie")
