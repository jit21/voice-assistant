from ast import main
from importlib.resources import path

import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
import pyttsx3 as py
import wikipedia as wiki


def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning......")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try :
            print("Recognizing.......")
            data=recognizer.recognize_google(audio)
            print(data)
            return data.lower()
        except sr.UnknownValueError:
            print("Not understanding") 


def speachtx(x):
    engine=py.init()
    voice=engine.getProperty("voices")
    engine.setProperty("voice",voice[1].id)
    rate=engine.getProperty("rate")
    engine.setProperty("rate",150)
    engine.say(x)
    engine.runAndWait()
# z=sptext()
# speachtx(z)    
# if __name__=="__main":
z=speachtx("sir please say password to access")
password=sptext()

if password.lower()=="ritesh":
       
        while True:
            data1=sptext().lower()
            if "your name"in data1:
                name="my name is ai ritesh"
                speachtx(name)
            elif "made you" in data1:
                data="our boss Ritesh Mondal made me"
                speachtx(data)
            elif "version"in data1:
                version="1.0.0"
                speachtx(version)
            elif "date of birth" in data1:
                dob="25th october 2022"
                speachtx(dob)
            elif "time"in data1:
                time=datetime.datetime.now().strftime("%I%M%p")
                speachtx(time)
            elif"youtube"in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "joke"in data1:
                joke=pyjokes.get_joke(language="en",category="Nutral") 
                speachtx(joke)
            elif "play music" in data1:
                 address=r"C:\Users\JIT\Desktop\extra"
                 listsong=os.listdir(address)
                 print(listsong)
                 os.startfile(os.path.join(address))
                 print(listsong)
                #  speachtx("sir please say the index number of song")
                #  index=sptext()
                 os.startfile(os.path.join(address,listsong[1])) 
            elif "god" in data1:
                speachtx("god meanse creator")
                
                
                speachtx("so jit kumar das is a 20 years old college student who create me to impress her girlfriend")
            elif "open facebok" in data1:
                webbrowser.open("https://www.facebok.com/")  
            elif "open instagram"in data1:
                webbrowser.open("https://www.instagram.com/")
            # elif "search" in data1:
            #     data2=data1[7:]
            #   f
            elif "exit" in data1:
                speachtx("thank you sir please come again latter")
                break
            elif "build you " in data1:
                speachtx("jit kumar das is a college student who made me for some fun")
            else :
                result=wiki.summary(data1,sentences=3)
                speachtx(result)
                

            time.sleep(3)
# else :
#     speachtx("Entered password was wrong please try again")
    




                



