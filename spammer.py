import time, pyautogui

print('''
*************************************************************************
                     WELLCOME TO SPAMBOT
*************************************************************************''')
while True:
    print('''Chose Spam file:
    0) Custom file (Edit the custom.txt file)
    1) The B-Movie
    2) fuck
    3) Macarena
    4) Pumped up kick
    5) Rapgod 
    6) Never gonna give you up
    7)FunnyFunny
    q) Quit
    ''')

    a = input("Selection: ")
    if a == "0":
        x = "custom.txt"
    elif a == "1":
        x = "beemovie.txt"
    elif a == "2":
        x = "fuck.txt"
    elif a == "3":
        x = "macarena.txt"
    elif a == "4":
        x = "pumpedupkick.txt"
    elif a == "5":
        x = "rapgod.txt"
    elif a == "6":
        x = "rickroll.txt"
    elif a == "7":
        x = "notfunny.txt"
    elif a == "q":
        break

    if not a == "q":
        print("You got 5 seconds to click into the text box")
        print("WARNING: DO NOT CLICK ANYTHING OR MOVE THE MOUSE WHEN THE BOT IS RUNNING *or you PC will crash*")
    
    time.sleep(5)
    f = open(x,'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
    
    print("Finish !")
    time.sleep(5)
    print('''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ''')
