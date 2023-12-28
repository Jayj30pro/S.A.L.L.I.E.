from tkinter import *
import time
import pyttsx3
import speech_recognition
from PIL import ImageTk, Image

speechSpeed = 170

def speak(phrase):
    speech = pyttsx3.init()
    speech.setProperty('rate', speechSpeed)
    speech.setProperty('voice', 'english+f2')
    speech.say(phrase)
    speech.runAndWait()



def listen(function):
    recognizer = speech_recognition.Recognizer()
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            speak("Go ahead I'm listening")
            print('ready')
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"You said {text}") #test line
            if function == "Note":
                note(text)
            else:
                processSpeech(text)
    except:
        speak("I'm sorry, but I did not get that")



def processSpeech(spokenWords):
    if "note" in spokenWords:
        listen("Note")
        speak("I'm getting my notepad ready")


    elif "list" in spokenWords:
        makeList()

    # elif "" in spokenWords:
    #     #next function()
    # elif "" in spokenWords:
    #     #next function()
    # elif "" in spokenWords:
    #     #next function()
    # elif "" in spokenWords:
    #     #next function()
    else:
        speak("I got nothing")
        print("I got nothing")

def makeList():
    speak("What is the first item on the list?")
    listen("List")


def writeToList(text):
    print("it has been noted ", text, " was added")

def note(text):
    notepad = open("notepad.txt","a")
    notepad.write(text)
    notepad.close()

def getNotes():
    notes = open("notepad.txt, rt")
    speak("Here are the notes")
    speak(notes.read())

speak("Hi, I'm sallie")
listen("start")
