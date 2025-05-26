#---------------Imports--------------#
import random 
import time
import threading
from Common import narrate, optionN
#--------------Misc Variables--------#
Age = 16
Name = ("")
Menu = 0
GotCard = False
Job = 0
Cash = 10
Money = 0
Password = 0
Pin = 1
ATMOp = 0
Tee = True
Timer = 0
global Days
Days = 0
global Worked
Worked = False

#-----------------------INTRODUCTION--------------------------#
narrate("|--------------------INTRODUCTION--------------------|")
narrate("This is your new life")
narrate("In the main menu you will selcect buy Typing a number what you want to do, but first")
Name = str(input("Whats your name!: "))
time.sleep(1)
print("Happy Birthday",Name,"youre 16 and heres £10 to start you of!")
time.sleep(1)
narrate("You have 364 days till you next birtday!")
narrate("Also 30 seconds in your world is 1 day here!")
narrate("Making your life")
narrate("Beep Boop...!")
narrate("1.2.3!")
#------------------Timer------------------#
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

timer_thread = threading.Thread(target=timer, daemon=True)
timer_thread.start()
# the only part im not 100% is the daemon, from looking online I know it means to allow the code to exit
# the rest I do understand and I managed to write after looking at a thew examples
# this is a multi thread and runs in the background in a subprogram
# its a timer which is all simple to understand I just needed to understand threading, and after taking about an hour of reading and looking at examples
# I understand know
# I know their are different methods to apporoch this however this is the most simple one and only uses a built in python import so doesnt need external downloading
# Its good I hope 
#-------------Menu-0------------------#

while Menu > 6 or Menu <= 0 :
    print("|--------------------MAIN-MENU--------------------|")
    time.sleep(0.5)
    print("Reset for days,Type (0)")
    time.sleep(0.5)
    print("Get bank card, Type (1)")
    time.sleep(0.5)
    print("Get a job,     Type (2)")
    time.sleep(0.5)
    print("Work shift,    Type (3)")
    time.sleep(0.5)
    print("Visit ATM,     Type (4)")
    time.sleep(0.5)
    print("Go out,        Type (5)")
    time.sleep(0.5)
    print("Visit parents, Type (6)")
    time.sleep(0.5)
    currentt = Days
    print(f"\n>>> Days elapsed so far: {currentt}\n")    
    
    try:
        time.sleep(0.5)
        Menu = int(input("Please select your next step!: "))
        time.sleep(0.5)
    except ValueError:
        time.sleep(0.5)
        optionN()
        Menu = 0

    if Menu > 6 or Menu < 0:
        time.sleep(0.5)
        optionN()
        Menu = 0
    Password = 0 
#---------------Menu-1-------------#
    if Menu == 1 and GotCard == False:
        Pin = random.randint(1000, 9999)
        print ("Your Pin is ", Pin, "\n")
        Menu = 0
        GotCard = True
        
    while Menu == 1 and GotCard == True:
        narrate("Hi, youve already got a card, incase you forgot: ")
        print ("Your Pin is ", Pin, "\n")
        Menu = 0

#--------------Menu-2---------------#
    while Menu == 2 and GotCard == True:
        narrate("\nWhat Job would you like sir?")
        narrate("McDonalds(1)")
        narrate("Asda store manager (2)")
        narrate("Doctor (3)")
        narrate("bussiness owner(4)")
        try:
            time.sleep(0.5)
            Job = int(input("Please select your Job!: "))
        except ValueError:
            narrate("Thats not an option!")
            narrate("Please try again!")
            Menu = 2
            Job = 0
        if Job > 4 or Job <= 0:
            narrate("Thats not an option!")
            narrate("Please try again!")
            Menu = 2
            Job = 0
        if  Job == 1 and GotCard == True:
            narrate("\nnice choice!")
            narrate("Your salary will be £60 per day!")
            narrate("You can come when ever you want!")
            Menu = 0
        if Job == 2 and GotCard == True:
            print ("\nExelent referances sir!")
            time.sleep(0.5)
            print ("Your salary will be £120 per day!")
            time.sleep(0.5)
            print("You can come when ever you want!")
            time.sleep(0.5)
            Menu = 0
        if Job == 3 and GotCard == True:
            print ("\nAmazing qualifications sir! ")
            time.sleep(0.5)
            print("Your salary will be £300 per day!")
            time.sleep(0.5)
            print("You can come when ever you want!")
            time.sleep(0.5)
            Menu = 0
        if Job == 4 and GotCard == True:
            print ("\nWell sir its an honour doing bussiness!")
            time.sleep(0.5)
            print("What would you like your bussiness to be called sir?")
            time.sleep(0.5)
            BussinessName = str(input("\nEnter the bussiness name here! "))
            time.sleep(0.5)
            print (BussinessName, "Will be the finest bussiness ever!")
            time.sleep(0.5)
            print("Your going to be earning around £200 a day!")
            time.sleep(0.5)
            Menu = 0
    while Menu == 2 and GotCard == False:
            time.sleep(0.5)
            print("\nSorry sir it appears you dont have a bank account.\nYoud be amazing but please come back later with a card\nYou can get a card by pressing (1) in the main selection area!\n")
            Menu = 0
#-----------------Menu-3----------------------#
    while Menu == 3:
        if Job == 0:
            print("\nYou dont have a job to work.")
            time.sleep(0.5)
            print("You can find a job by pressing 2 in the main selection!")
            time.sleep(0.5)
            Menu = 0
        if Job == 1 and Worked == False:
            print("\nBeep boop!")
            time.sleep(0.5)
            print("Ill have one double chease burger with a large frie please")
            time.sleep(0.5)
            print("You have worked a day!\nTotal earnings : £60")
            time.sleep(0.5)
            Money = Money + 60
            print("You now have a whole £",Money,"!")
            time.sleep(0.5)
            Worked = True
            Menu = 0
        if Job == 2 and Worked == False:
            print("\nSir what shall I do?")
            time.sleep(0.5)
            print("I quit")
            time.sleep(0.5)
            print("IM HIRED!")
            time.sleep(0.5)
            print("You have worked a day!")
            time.sleep(0.5)
            print("Total earnings : £120")
            time.sleep(0.5)
            Money = Money + 120
            print("You now have a whole £",Money,"!")
            time.sleep(0.5)
            Worked = True
            Menu = 0
        if Job == 3 and Worked == False:
            print("\nScalpul...")
            time.sleep(0.5)
            print("Beep Beep Beeeeeeeeep")
            time.sleep(0.5)
            print("Defibrillator now!")
            time.sleep(0.5)
            print("HES ALLIVE!")
            time.sleep(0.5)
            print("You have worked a day!")
            time.sleep(0.5)
            print("Total earnings : £300")
            time.sleep(0.5)
            Money = Money + 300
            print("You now have a whole £",Money,"!")
            time.sleep(0.5)
            Worked = True
            Menu = 0
        if Worked == True:
            print("\nYouve already worked today, your going to have to come back tomorrow!\n")
            time.sleep(0.5)
            Menu = 0
#------------------------------Menu-4--------------------------#
    while Menu == 4 and GotCard == True:
        while Password != Pin and Password != 1:
            print("Welcome to the ATM,")
            try:
                time.sleep(0.5)
                print("You can press (1) to leave")
                Password = int(input("Please enter your pin: "))
                time.sleep(0.5)
            except ValueError:
                time.sleep(0.5)
                Password = 0
            if Password == 1:
                print("\nYou left the ATM!\n")
                Password = 1
                Menu = 0
            if Password > 9999 or Password < 1000 and Password > 0 and Password != 1:
                time.sleep(0.5)
                print("Thats not a 4 digit pin!")
                print("Please try again")
                Password = 0
            if Password == Pin:
                Con = 0
                Con = Con + 1
                if Con == 1:
                    print("Validating")
                    time.sleep(1)
                    print("Accepted!")
                    time.sleep(1)
        while Password == Pin and ATMOp <= 0 or Password == Pin and ATMOp > 5:
            print("Please select an option")
            print("Check balance,     (1):")
            print("Check cash on you, (2):")
            print("Withdraw money,    (3):")
            print("Deposite money,    (4):")
            print("Leave ATM,         (5):")
            try:
                time.sleep(0.5)
                ATMOp = int(input("Please select your option here: "))
                time.sleep(0.5)
            except ValueError:
                time.sleep(0.5)
                ATMOp = 0
            if ATMOp > 5 or ATMOp <= 0:
                print("Thats not an option")
                print("Please try again")
#-----------------------------------------
            while ATMOp == 1:
                print("You have £",Money,",in your bank account!")
                ATMOp = 0
#-------------------------------------------
            while ATMOp == 2:
                print("You have £",Cash,"Currently on your person!")
                ATMOp = 0
#---------------------------------------
            while ATMOp == 3:
                print("How much money would you like to withdraw")
                print("Press (0) to abort transaction")
                
                try:
                    AmountW = int(input("\nEnter here: "))
                except ValueError:
                    AmountW = 1
                    print("\nPlease enter a number")
                    
                if AmountW < 0 :
                    print("\nYou cant withdraw nothing")
                    print("Please try again")
                    AmountW = 1
                    
                if AmountW > Money:
                    print("\nYou only have £",Money," in your account")
                    print("Please try again")
                    AmountW = 0
                    
                if AmountW <= Money and AmountW > 1:
                    print("\nTransacting")
                    print("BeepBoop")
                    Money = Money - AmountW
                    Cash = Cash + AmountW
                    print("Transaction complete!")
                    print("\nYou now have £",Money," in your bank account")
                    print("You now have £",Cash," in cash on your person")
                    ATMOp = 0
                    AmountW = 1
                if AmountW == 0:
                    ATMOp = 0
#-------------------------------------------------------
            while ATMOp == 4:
                print("How much money would you like to deposite")
                print("Press (0) to abort transaction")
                
                try:
                    AmountD = int(input("\nEnter here: "))
                except ValueError:
                    AmountD = 1
                    print("\nPlease enter a number")
                    
                if AmountD < 0 :
                    print("\nYou cant deposite nothing")
                    print("Please try again")
                    AmountD = 1
                    
                if AmountD > Cash:
                    print("\nYou only have £",Cash," on you!")
                    print("Please try again")
                    AmountD = 0
                    
                if AmountD <= Money and AmountD > 1:
                    print("\nTransacting")
                    print("BeepBoop")
                    Money = Money + AmountD
                    Cash = Cash - AmountD
                    print("Transaction complete!")
                    print("\nYou now have £",Money," in your bank account")
                    print("You now have £",Cash," in cash on your person")
                    ATMOp = 0
                    AmountD = 1
                if AmountD == 0:
                    ATMOp = 0
    while Menu == 4 and GotCard == False:
        print("You dont have a card yet!")
        print("You can get a card by pressing (1) in the menu!")
        Menu = 0 
        
        
