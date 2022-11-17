from tkinter import *
import speech_recognition as sr
import webbrowser 
import pyttsx3
from datetime import datetime
import subprocess

root=Tk()
root.geometry("500x500")
root.configure(bg="light blue")

label=Label(root,text="Welcome To Your Personal Desktop Assistant",bg="light blue",font=("Bahnschrift light",15,"bold"))
label.place(relx=0.5,rely=0.15,anchor=CENTER)

label1=Label(root,text="Crafted with 💖💖 by Riyaaa",bg="light blue",font=("Bahnschrift light",15,"bold"))
label1.place(relx=0.5,rely=0.25,anchor=CENTER)

text_to_speech=pyttsx3.init()
def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speak("How can i help you...?")
    speech_recognisor=sr.Recognizer()
    with sr.Microphone() as source:
        audio=speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data=speech_recognisor.recognize_google(audio,language='en-in')
        except sr.UnkownValueError:
            print("Please repeat I did not get that")
            speak("Please repeat i did not get that")
   
    respond(voice_data)
    
def respond(voice_data):
    voice_data=voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Apollo & Riya is awsome")
        print("My name is Apollo")
        
    if "time" in voice_data:
        speak("The Current time is ")
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
        
    if "google" in voice_data:
        speak("Opening Google")
        print("Opening Google")
        webbrowser.get().Popen(["https://google.com"])
        
    if "videos" in voice_data:
        speak("Opening YouTube")
        print("Opening YouTube")
        webbrowser.get().open(["https://youtube.com"])
    
    if "notepad" in voice_data:
        speak("Opening notepad")
        print("Opening notepad")
        subprocess.Popen(["notepad.exe"])  
        
    if "Billie Eilish" in voice_data:
        speak("Opening YouTube Billie Eilish Mix")
        print("Opening YouTube Billiue Elish Mix")
        webbrowser.get().Popen(["https://www.youtube.com/watch?v=topHZSXDpws"])
    
btn=Button(root,text="Activate",bg="purple",fg="white",padx=10,pady=1,font=("Arial",11,"bold"))
btn.place(relx=0.5,rely=0.5,anchor=CENTER)    
root.mainloop()
        
    