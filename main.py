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

            if function == "Note":
                note(text)
            
            if function == "List":
                writeToList(text)

            
            else:
                processSpeech(text)
    except:
        speak("I'm sorry, but I did not get that")


        


def processSpeech(spokenWords):
    if "note" in spokenWords:
        speak("I'm getting my notepad ready")
        listen("Note")

    if "list" in spokenWords:
        speak("What is the first item on the list?")
        listen("List")

    if "what" and "got" in spokenWords:
        getNotes()

    if "what" and "agenda" in spokenWords:
        readList()

    # elif "" in spokenWords:
    #     #next function()
    # elif "" in spokenWords:
    #     #next function()
    # elif "" in spokenWords:
    #     #next function()

    else:
        speak("I got nothing")
        print("I got nothing")


    

def readList():
    print('here is what is on the agenda')
    agenda = open("theList.txt", "rt")
    speak("Here is what is on the agenda")
    speak(agenda.read())
    agenda.close()

def writeToList(text):
    theList = open("theList.txt","a")
    theList.write(text + "\n")
    theList.close()
    speak("Got it.", text, ", was added to the list")



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

def intro():
    speak("Hi, I'm sallie. I am your personal digital assistant, You can tell me what you want me to do or say, nevermind, to use the buttons")

intro()
#getNotes()
listen("start")

#listen()
