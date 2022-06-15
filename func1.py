import speech_recognition as sr
import playsound
import wikipedia as wiki
import datetime
import wolframalpha
import selenium 
from gtts import gTTS
import webbrowser as wb
import google
import pyaudio
import os
import requests
import time
import urllib
import subprocess

speak = sr.Microphone()
rec = sr.Recognizer()

with speak as source:
    rec.adjust_for_ambient_noise(source)
    listen = rec.listen(source) 
    roma = gTTS(text = "how can i help you?", lang = 'en', slow = False)
    roma.save("rep.mp3")
    os.system("rep.mp3")
    time.sleep(5)

with speak as ansource:
    rec.adjust_for_ambient_noise(ansource)    
    print("yes?")
    listen_again = rec.listen(ansource)
    text = rec.recognize_google(listen_again)
    print(text)
    time.sleep(4)
    if "Google" in text:
        wb.open("https://www.google.com")
    elif "Youtube" in text:
        wb.open("https://youtube.com")
    elif "wikipedia" in text:
        wb.open("https://www.wikipedia.org/")
    elif "udemy" in text:
        wb.open("https://www.udemy.com/")
    elif "instagram" in text:
        wb.open("https://www.instagram.com/")
    elif "spotify" in text:
        wb.open("http://www.spotify.com/")    
       
    
    elif "what is your name" in text:
        reply1 = gTTS(text = "Hey! my name is roma",lang = "en", slow = False)
        reply1.save("what.mp3")
        os.system("what.mp3")
    elif "who created you" in text:
        reply2 = gTTS(text = "I was created and being maintained by akshay karanwal",lang = 'en',slow = False)
        reply2.save("who.mp3")
        os.system("who.mp3")
    elif "how you could help me" in text:
        reply3 = gTTS(text = "Well, as i am constantly being updated by my creator so there is a little possibility that i can't help you out at a point but i will try my best sir.", lang = 'en',slow = False)
        reply3.save("how.mp3")
        os.system("how.mp3")
          
           # add more personal / theoritical questions

           
    
    app_id = 'EW9QTP-VGE4TG6R56'
    client = wolframalpha.Client(app_id)
    result = client.query(text)
    for pod in result.pods:
        for sub in pod.subpods:
            print(sub.plaintext)
            reply3 = gTTS(text = sub.plaintext, lang = 'en', slow = False)
            reply3.save("info.mp3")
            os.system("info.mp3")
     
    

        
        
    
   




     
     



   
 
    
    
