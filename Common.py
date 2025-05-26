import random 
import time
import threading
#-------Timer-------
def timer():
    global Days
    Timer = 0
    global Worked
    Worked = False
    while True:
        time.sleep(1)
        Timer += 1
        if Timer >= 30:
            Days += 1
            Worked = False
            Timer = 0
# the only part im not 100% is the daemon, from looking online I know it means to allow the code to exit
# the rest I do understand and I managed to write after looking at a thew examples
# this is a multi thread and runs in the background in a subprogram
# its a timer which is all simple to understand I just needed to understand threading, and after taking about an hour of reading and looking at examples
# I understand know
# I know their are different methods to apporoch this however this is the most simple one and only uses a built in python import so doesnt need external downloading
# Its good I hope 

#------------narrate---------
seconds_per_message = 1

def narrate(message):
    print(message)
    time.sleep(seconds_per_message)
def optionN():
    narrate("Thats not an options!")
    narrate("Please try again!")