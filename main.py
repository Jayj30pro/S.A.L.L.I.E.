#from tkinter import *
#import time
import pyttsx3
import speech_recognition
#from PIL import ImageTk, Image

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
            print('ready')
            speak("Go ahead I'm listening")
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"You said {text}") #test line

            if function == "start":
                processSpeech(text)

            elif function == "Note":
                note(text)

            
            else:
                processSpeech(text)
    except:
        speak("I'm sorry, but I did not get that")


        


def processSpeech(spokenWords):
    if "note" in spokenWords:
        speak("I'm getting my notepad ready")
        listen("Note")
        
    elif "what" and "got" in spokenWords:
        print("notes")
        getNotes()

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
    notepad.write(text + "\n")
    notepad.close()

def getNotes():
    print('here are the notes')
    notes = open("notepad.txt", "rt")
    speak("Here are the notes")
    speak(notes.read())
    notes.close()

speak("Hi, I'm sallie")
#getNotes()
listen("start")

#listen()
