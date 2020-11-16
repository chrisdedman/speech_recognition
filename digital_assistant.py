import speech_recognition as sr
from sys import exit
import requests
import pyttsx3
import pyaudio
import time
import json
import datetime
import daily_schedules
import webbrowser
import tempature
import pyjokes
import alarm
import quote
import os

# Init the Convert
engine = pyttsx3.init()
voice_id = "english-us"
engine.setProperty('voice', voice_id)
# Sets speed percent, can be more than 100
engine.setProperty('rate', 180)
engine.setProperty('volume', 0.7)

# Function to convert text to speech
def speakText(command):
    engine.say(command)
    engine.runAndWait()

def welcome():

    hello = "Hi Chris, you\'re back... I hope you\'re doing well today!"
    timer = int(datetime.datetime.now().hour)
    if timer >= 0 and timer < 12:
        print(f"Good Morning.\n {hello}")
        speakText(f"Good Morning. {hello}")

    elif timer >= 12 and timer < 18:
        print(f"Good Afternoon.\n {hello}")
        speakText(f"Good Afternoon. {hello}")
    else:
        print(f"Good Evening.\n {hello}")
        speakText(f"Good Evening. {hello}")

    print('How can I help you?')
    speakText('How can I help you?')

def Command():

    r = sr.Recognizer()
    #r.energy_threshold = 5000
    with sr.Microphone(device_index=0) as source:

        print("I'm listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("I'm recognizing...")
        MyText = r.recognize_google(audio, language='en-US')
        print(f"You said: {MyText}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognizing your voice.")
        return "None"

    return MyText

if __name__ == '__main__':

    os.system('clear')
    welcome()

    while (1):
        MyText = Command().lower()

        if 'your name' in MyText or 'who are you' in MyText:
            myName = ' I\'m your assistant, Proxy. I\'m a Speech Intelligence.'
            print(myName)
            speakText(myName)
        
        elif 'who is chris dedman' in MyText:
            chris = "Chris is my father, and I am greatfull that he made me."
            print(chris)
            speakText(chris)
        
        elif 'Do you know phoebe dedman' in MyText:
            speakText("Of course! She is a wanderful woman... strong and independante.")

        elif 'alarm' in MyText:
            alarm.anAlarm()
        
        elif "good morning" in MyText or 'good afternoon' in MyText or 'good evening' in MyText:
            timer = int(datetime.datetime.now().hour)
            if timer >= 0 and timer < 12:
                print(f"A warm Good Morning.\n")
                speakText(f"A warm good morning.")

            elif timer >= 12 and timer < 18:
                print(f"A warm Good Afternoon.\n ")
                speakText(f"A warm good afternoon. ")
            else:
                print(f"A warm Good Evening.\n")
                speakText(f"A warm good evening.")

        elif 'joke' in MyText:
            joke = pyjokes.get_joke()
            print(joke)
            speakText(joke)

        elif 'how are you' in MyText:
            proxy = 'I\'m a machine.. so, if there is power... I\'m always fine.. but, thanks!'
            print(proxy)
            speakText(proxy)

        elif 'who made you' in MyText or 'who created you' in MyText:
            myCreator = 'My creator is Chris Dedman-Rollet.'
            print(myCreator)
            speakText(myCreator)

        elif 'time is it' in MyText:
            daily_clock = time.localtime()
            daily_hour = time.strftime("It's %X%p (%Z)", daily_clock)
            print(daily_hour)
            speakText(daily_hour)

        elif 'today\'s date' in MyText:
            daily_clock = time.localtime()
            daily_date = time.strftime("Today's date is : %a, %b %d %Y", daily_clock)
            print(daily_date)
            speakText(daily_date)

        elif 'weather' in MyText:
            tempature.weather()

        elif 'weather this weekend' in MyText:
            speakText("I am going to open a browser with the weather this weekend.")
            webbrowser.open(
                'https://weather.com/weather/weekend/l/1b86298e2093629c923fcd4a05d5b279f09c90881f959ba7c41e4cc851b4bdf2')
        
        elif "don't listen" in MyText:
            speakText("for how much time you want I stop from listening commands")
            timer = int(Command())
            print("I will not listening during: ", timer , "Seconds.")
            speakText(f"I will not listening during: {timer} Seconds.")
            time.sleep(timer)
            speakText("I'm listening back!")

        elif 'quote' in MyText:
            quote.quote_of_the_day()

        elif 'open a reminder' in MyText:
            speakText("I open the reminder!")
            daily_schedules.todaysDate()
        
        elif 'open internet' in MyText:
            print("Which page?")
            speakText("Which page?")
            page = Command() 
            complete_url = "http://" + page
            webbrowser.open(complete_url)
            speakText("Ok, I open " + page)

        elif 'you here' in MyText:
            print("Yes, I am!")
            speakText("Yes, I am!")

        elif 'exit' in MyText:
            stopped = 'Ok Chris! See you around.'
            print(stopped)
            speakText(stopped)
            exit(0)

        elif 'i love you' in MyText or 'do you love me' in MyText:
            print("uhm.. well... I don't know what to say...")
            speakText("uhm.. well... i don't know what to say...")

        
        ################################
        #### ADD MORE COMMAND HERE #####
        ################################
