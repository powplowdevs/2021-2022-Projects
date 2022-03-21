#Copyright © 2021 Powplowdevs

import keyboard
import time
import random
import string
import sys
import threading



#this list has all the possible actions codes for the keyboard later on in the code 
#a random object will be pulled from the list and based on it we will run one of our functions
obs = ["KL", "PU", "PD", "PS", "PR", "PB", "F1", "F12", "W", "WINS", "CZ", "CY", "CC", "CV", "RL", "tabe"]

#this is used for for the random letter attack its just a list with the entire alphabet
alpabe = string.ascii_lowercase + string.digits + string.ascii_uppercase 

#our vars for later on
score = -1
level = 1
num = 0
nums = 1
cap = 10

#the start function it tells the story of the keyboard
def start():
    coms = input("to skip intro type [skip] else type anything: ")
    if coms == "skip":
        endit.start()
        main()
    else:
        print("downloading")
        time.sleep(1)
        print("downloading.")
        time.sleep(1)
        print("downloading..")
        time.sleep(1)
        print("downloading...")
        time.sleep(1)
        print("complte!")
        time.sleep(1)
        print("hi im keybord-super-v69420")
        time.sleep(2.5)
        print("i am a new and improved keybord for you!")
        time.sleep(2.5)
        print("i will never turn on you")
        time.sleep(2.5)
        print("or hurt you!")
        time.sleep(3)
        print("...")
        time.sleep(3)
        print("wait?")
        time.sleep(2.5)
        print("y...you")
        time.sleep(2.5)
        print("YOU WHERE GONNA HIT MY KEYS?!?!?!?")
        time.sleep(2.5)
        print("no way! i cant let you do that!")
        time.sleep(2.5)
        print("THIS ENDS NOW!")
        time.sleep(2.5)
        print("good luck typeing! >:}")
        time.sleep(1)
        print("here is the game plan!")
        time.sleep(1)
        print("lots of attacks will be trown at you to avoid the you can do these 3 things!")
        time.sleep(1)
        print("just deal with it! DUH")
        time.sleep(1)
        print("spam or hold esc")
        time.sleep(1)
        print("spam or hold crtl")
        print("   ")
        print("good luck!...you'l need it >:{")
        
        time.sleep(5)
        endit.start()
        main()

#our main functions it is what runs all the attacks based on a random object we pulled form the obs list (see line 13)
def main():
    global score
    global level
    global nums
    global num
    global cap
    
    print("   ")
    print("HEY IF YOU GET STUCK IN A BAD SPOT JUST CLICK ON THE TERMINAL AND PRES ctrl+c or alt+f4")
    print("   ")
    
    if nums == 0:
        score = score + 1

    
    print("score is :", score)
    print("level is :", level)
      
    do = random.choice(obs)
    wait = random.randrange(5, 15)
    if nums == 0:
        time.sleep(wait)
        nums = 1
    
    if num == cap:
        print("hmm looks like ima need to take this to the next level!")
        time.sleep(1)
        level += 1
        print("to level: ", level)
        num = 0
        if cap == 30:
            print("this is the final level it cant get any harder just goes downhill form here for u! }:>")
        else:
            cap = cap + 10
    else:
        num += 1
    
    

    
    if do == obs[0] and level >= 3:
        nums = 0
        key_log()
    if do == obs[1] and level >= 1:
        nums = 0
        page_up()
    if do == obs[2] and level >= 1:
        nums = 0
        page_down()
    if do == obs[3] and level >= 1:
        nums = 0
        press_shift()
    if do == obs[4] and level >= 1:
        nums = 0
        press_s()
    if do == obs[5] and level >= 2:
        nums = 0
        pbs()
    if do == obs[6] and level >= 2:
        nums = 0
        hf1()
    if do == obs[7] and level >= 3:
        nums = 0
        hf12()
    if do == obs[8] and level >= 3:
        nums = 0
        writes()
    if do == obs[9] and level >= 1:
        nums = 0
        win()
    if do == obs[10] and level >= 2:
        nums = 0
        hcz()
    if do == obs[11] and level >= 2:
        nums = 0
        hcy()
    if do == obs[12] and level >= 1:
        nums = 0
        cc()
    if do == obs[12] and level >= 1:
        nums = 0
        cv()
    if do == obs[14] and level >= 1:
        nums = 0
        random_let()
    if do == obs[15] and level >= 2:
        nums = 0 
        tabs()
      
    
    main()

#stop function pretty self explanatory it stops the code based on a input
def stop():
    print("   ")
    print("   ")
    command = input("end the suffering? ")# dont wrry abt this part 
    print("   ")
    if "yes" in command:
        print(f"geuss you just couldent take it anymore huh? {score} was your score. goodluck with the old keyboard")
        sys.exit()
        quit()
    

######################################################

#everything under this until the hashtag line is out attack functions used in the main functions (see line 82)
        
#code: KL
def key_log():
    recorded = keyboard.record(until='esc')
    try:
        while True:
            if not keyboard.is_pressed("ctrl"):
                keyboard.play(recorded, speed_factor=2.5) 
            else:
                main()
                
  
         
        
    except: 
            print("key logger ended")
            main()
                   
#code: PU
def page_up():
    keyboard.press("page up")
    time.sleep(1)
    keyboard.release("page up")
    main()
        
#code: PD
def page_down():
    keyboard.press("page down")
    time.sleep(1)
    keyboard.release("page down")
    main()
        
#code: PS
def press_shift():
    keyboard.press("caps lock")
    main()
        
#code: PR
def press_s():
    keyboard.press("space")
    time.sleep(1)
    keyboard.release("space")
    time.sleep(1)
    keyboard.press("space")
    time.sleep(1)
    keyboard.release("space")
    time.sleep(1)
    keyboard.press("space")
    time.sleep(1)
    keyboard.release("space")
    time.sleep(1)
    keyboard.press("space")
    time.sleep(1)
    keyboard.release("space")
    time.sleep(1)
    keyboard.press("space")
    time.sleep(1)
    keyboard.release("space")
    main()
        
#code: F1
def hf1():
    keyboard.press("f1")
    time.sleep(1)
    keyboard.release("f1")
    main()
            
#code: F12
def hf12():
    keyboard.press("f12")
    time.sleep(1)
    keyboard.release("f12")
    main()
        
#code: W
def writes():
    keyboard.write('dang this must be getting super anyoning.')
    main()
        
#code: WINS
def win():
    keyboard.press("windows")
    time.sleep(1)
    keyboard.release('windows')
    main()
     
#code: CZ
def hcz():
    keyboard.press("ctrl")
    keyboard.press("z")
    time.sleep(1)
    keyboard.release('ctrl')
    keyboard.release('z')
    main()
            
#code: CY
def hcy():
    keyboard.press("ctrl")
    keyboard.press("y")
    time.sleep(1)
    keyboard.release('ctrl')
    keyboard.release('y')
    main()
        
#code: CC
def cc():
    keyboard.press("ctrl")
    keyboard.press("a")
    time.sleep(1)
    keyboard.release('ctrl')
    keyboard.release('a')
    keyboard.press("ctrl")
    keyboard.press("c")
    time.sleep(1)
    keyboard.release('ctrl')
    keyboard.release('c')
    main()
        
#code: CV
def cv():
    
    keyboard.press("ctrl")
    keyboard.press("v")
    time.sleep(1)
    keyboard.release('ctrl')
    keyboard.release('v')
    main()
        
#code: RL
def random_let():
    
    let = random.choice(alpabe)
    keyboard.write(let)
    main()

#code: PB
def pbs():
    
    keyboard.press("backspace")
    time.sleep(1)
    keyboard.release("backspace")
    keyboard.press("backspace")
    time.sleep(1)
    keyboard.release("backspace")
    keyboard.press("backspace")
    time.sleep(1)
    keyboard.release("backspace")
    keyboard.press("backspace")
    time.sleep(1)
    keyboard.release("backspace")
    keyboard.press("backspace")
    time.sleep(1)
    keyboard.release("backspace")
    keyboard.press("backspace")
    time.sleep(1)
    keyboard.release("backspace")
    keyboard.press("backspace")
    time.sleep(1)
    keyboard.release("backspace")
    main()
 
#code: tabe
def tabs():
    
    keyboard.press("tab")
    time.sleep(1)
    keyboard.release("tab")
    time.sleep(.1)
    keyboard.press("shift")
    keyboard.press("tab")
    time.sleep(1)
    keyboard.release("tab")
    keyboard.release("shift")
 
######################################################

#a thread is used to make sure the end functions is always ready to kill the script }:>
endit = threading.Thread(name='ends', target=stop)  

#start the while loop
start()

#dont steal that mean >:
# __author__ = "Powplowdevs"
# __copyright__ = "Copyright (C) 2021 Powplowdevs"
# __version__ = "1.0"