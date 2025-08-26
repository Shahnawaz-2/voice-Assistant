import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "41fb3bab195a4a53b4aaa19115a544be"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="AIzaSyBVypj20Ik37SkxQpYQ0hb8WA4Zan4pJlE",
   )
    completion = client.chat.completions.create(
    model ="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "you are a virtual assistant named jarvis skilled in genral tasks like Alexa and Google Cloud"},
        {"role": "user", "content":command}
    ]
    )
    return completion.choice[0].message.content
 
   


   
def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
   elif "open instagram" in c.lower():
      webbrowser.open("https://instagram.com")       
   elif c.lower().startswith("play"):
      song = c.lower().split(" ")[1]
      link = musiclibrary.music[song]
      webbrowser.open(link)

   elif "news" in c.lower():
      r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=41fb3bab195a4a53b4aaa19115a544be")
      if r.status_code == 200:

          data = r.json()

          articles = data.get('articles', [])

          for article in articles:
            speak(article['title'])   
   else:

      # Let OpenAi handle the request
      output = aiProcess(c)
      speak(output)
 


if __name__ == "__main__":
    speak("Initializing Jarvis...")

while True:
    r = sr.Recognizer()
    

      
    print("recognizing...")
    try:
       with sr.Microphone() as source:
         print("Listening...")
         audio = r.listen(source, timeout=2, phrase_time_limit=1) 
       word = r.recognize_google(audio)
       if(word.lower()=="jarvis"):
        speak("ya")
        with sr.Microphone() as source:
           print("Jarvis Active...")
           audio = r.listen(source)
           command = r.recognize_google(audio)

           processCommand(command)

    

    except Exception as e:
        print("google error; {0}".format(e))           