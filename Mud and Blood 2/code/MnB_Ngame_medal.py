# program for achieving the play n games medals

import os
import keyboard
import time

def ciclo():

    # 0
    os.startfile("C:\Afonso_2\Jogos\Mud and Blood 2.exe")
    time.sleep(8)

    #1
    keyboard.press_and_release('tab, tab, enter')
    time.sleep(1)
    
    #2
    keyboard.press_and_release('tab, tab, tab, enter')
    time.sleep(1)

    # 8
    keyboard.press_and_release('alt+F4')
    time.sleep(1)

n=0

while n<8:
    ciclo()
    n+=1