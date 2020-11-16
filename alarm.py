import datetime
import pyttsx3
import speech_recognition as sr
import os
import digital_assistant

engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 0.7)

def speakText(command):
    engine.say(command)
    engine.runAndWait()

def Commands():
    
    r = sr.Recognizer()
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

def anAlarm():
    print("I'll setup an Alarm for you!")
    speakText("I will setup an alarm for you")

    while (1):
        print("Set hour: ")
        speakText("Set hour: ")
        alarm_hour = int(Commands())

        print("Set minutes: ")
        speakText("Set minutes: ")
        alarm_minutes = int(Commands())

        print("Am or Pm? ")
        speakText("a.m. or p.m.?")
        am_pm = Commands()

        print(f"Waiting for time: {alarm_hour}:{alarm_minutes} {am_pm}")

        # time conversion
        # because datetime module returns time in military form i.e. 24 hrs format
        if am_pm == 'p.m.':  # to convert pm to military time
            alarm_hour += 12

        elif alarm_hour == 12 and am_pm == 'a.m.':  # to convert 12am to military time
            alarm_hour -= 12

        else:
            pass

        while True:  # infinite loop starts to make the program running until time matches alarm time

            # ringing alarm + execution condition for alarm
            if alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute:

                print("\nIt's the time!")
                speakText("Chris, It is the time. WAKE UP!")
                print("What can I do for you now?")
                speakText("what can I do for you now?")
                return digital_assistant.Command()