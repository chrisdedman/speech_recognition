from sys import exit
# from AppKit import NSSound
import time
import os
import pyttsx3
from datetime import datetime

# ----------------------------------------------------- #
# -- Create a list where to save your daily reminder -- #
# ----------------------------------------------------- #
list = []
# ----------------------------------------------------------------------- #
# --- Here's your daily date append in the file: history_reminder.txt --- #
# ----------------------------------------------------------------------- #
def todaysDate():
    daily_clock = time.localtime()
    daily_date = time.strftime("%a, %b %d %Y", daily_clock)
    data = "----------------\n" + daily_date + "\n----------------"
    with open("history_reminder.txt", 'a') as output:
        output.write("\n" + data + '\n')
        output.close()
        return Alarm()
# ------------------------------- #
# -- Set up your reminder here -- #
# ------------------------------- #
def Alarm():
    global list
    end_time1 = input("At what time do you want an alarm?\n(Format 24h: hh:mm:ss)\n>>")
    reminder = input("What's the reminder for?\n>>")
    # --------------------------------------------- #
    # -- Append your reminder in list = [] above -- #
    # --------------------------------------------- #
    all = "Time: " + end_time1 + " Your Reminder is: " + reminder
    list.append(all)
    # ---------------------------------------------------------------------------- #
    # -- Here you append your history to the history file: history_reminder.txt -- #
    # ---------------------------------------------------------------------------- #
    with open("history_reminder.txt", 'a') as output:
        output.write(all + '\n')

    Last_reminder = input("Do you want to see your all reminder schedules?\n[yes/no]\n>>")
    if 'yes' in Last_reminder:
        print(list)
        question = input("Are you done?")
        if 'yes' in question:
            pass
    else:
        pass

    its_time = False
    while its_time == False:
        its_time = False
        # ------------------------------------------ #
        # ------ Local Time in your country! ------- #
        # ------------------------------------------ #
        clock = time.localtime()  # get struct_time
        Timer = time.strftime("%a, %b %d %Y, %X%p (%Z)", clock)
        # ------------------------- #
        # ------ Timer Loop ------- #
        # ------------------------- #
        if end_time1 in Timer:
            its_time = True
            print("Your Reminder is:\n(",reminder,")")
            pyttsx3.speak(reminder)
            # ----------------------------- #
            # ------ Prepare Sounds ------- #
            # ----------------------------- #
            # sound = NSSound.alloc()
            # sound.initWithContentsOfFile_byReference_(
            #     'reminder_voice.mp3', True)
            # sound.play()
            # ------------------------------------------------------------ #
            # ------ Add 8 seconds time sleep (time the song play) ------- #
            # ------------------------------------------------------------ #
            time.sleep(8)
            # while sound.isPlaying():
            another = input("Do you want an other one?\n[yes/no]\n>>")
            if another == 'yes':
                return Alarm()
            else:
                # -------------------------------------------- #
                # -- Here you print the history of your day -- #
                # -------------------------------------------- #
                print(list)
                break
            # --------------------------------------------- #
            # ------ Print this until the time out! ------- #
            # --------------------------------------------- #
        else:
            start = time.strftime("%X")
            format = '%H:%M:%S'
            time_left = datetime.strptime(end_time1, format) - datetime.strptime(start, format) # Subtract the time left before end time.

            print("." * 50)
            print("Local current time :", Timer)
            print("\tTimer end at: ", end_time1)
            print("\tYour reminder is:", reminder)
            print("\tTime left: ", time_left)
            print("." * 50)

            time.sleep(1)
            os.system('clear')
            its_time = False

if __name__ == "__main__":
    todaysDate()
