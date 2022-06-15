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

recognize = sr.Recognizer()
user_question = sr.Microphone()
with user_question as source:
    print("Hey there mate! how can i help you ?")
    listen = recognize.listen(source)
    print(recognize.recognize_google(listen))


app_id = 'EW9QTP-VGE4TG6R56'
client = wolframalpha.Client(app_id)
res = client.query(user_question)
answer = next(res.results)
print(answer)



