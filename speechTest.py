import speech_recognition as sr
import pyttsx3
from sys import exit
import TimerTry
import webbrowser

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Loop infinitely, speak infinitely.
while (1):
    try:
        # Set up your microphone as source of input
        # // Use sr.Microphone.list_microphone_names()
        # to know the index of you microphone do you have //
        mic = sr.Microphone(device_index=0)

        with mic as source:
            # Wait for a second to let the recognizer adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source, duration=0.2)
            # Listen the user input
            audio = r.listen(source)

            # Recognize audio with google
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()

            print("You said: ", r.recognize_google(audio))
            SpeakText(MyText)
            
            ###################################################
            #### Feel Free to add more command behind that ####
            ###################################################
            if 'yes' in MyText:
                print("Test Passed!")
            # If you said open a reminder (my other script) the script will open the other program. (feel free to try with your own script)
            elif 'open a reminder' in MyText:
                TimerTry.todaysDate()
            # This next few line of code will open spesific task (according with what you will say) feel free to add more command.
            elif 'open facebook' in MyText:
                webbrowser.open('http://facebook.com')
            
            elif 'open ig' in MyText:
                webbrowser.open('http://instagram.com')
                
            elif 'open cisco' in MyText:
                webbrowser.open('http://cisco.com')
            # Here if you say stop in your sentence (exemple: can you please STOP the program #AlwaysBeKind, the script will stop.
            elif 'stop' in MyText:
                print("Test Passed!")
                exit(0)
            else:
                pass

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    # If your speech is not clear.
    except sr.UnknownValueError:
        print("unknown error occured")
