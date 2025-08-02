import os
import keyboard
import time

def ciclo():

    # 0
    os.startfile("C:\Afonso_2\Jogos\Mud and Blood 2.exe")
    time.sleep(5)

    #1
    keyboard.press_and_release('tab, tab, enter')
    time.sleep(0.5)

    #2
    keyboard.press_and_release('tab, tab, tab, tab, enter')
    time.sleep(0.5)

    #3
    keyboard.press_and_release('shift+tab, shift+tab, shift+tab, shift+tab, shift+tab, shift+tab, shift+tab, shift+tab, enter')
    time.sleep(0.5)

    #4
    n=0
    while n<2:
        keyboard.press_and_release('2, 4')
        time.sleep(20.1)
        n+=1

    #5 surrender
    keyboard.press_and_release('2, 6')
    time.sleep(0.5)

    # 8
    keyboard.press_and_release('alt+F4')

    # 9 iniciar 
    os.startfile("C:\Afonso_2\Jogos\Mud and Blood 2.exe")
    time.sleep(5)

    #1
    keyboard.press_and_release('tab, tab, enter')
    time.sleep(0.5)

    #2
    keyboard.press_and_release('tab, tab, tab, tab, enter')
    time.sleep(0.5)

ciclo()