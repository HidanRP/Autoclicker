import keyboard as kb
import pyautogui as gui
import time as t

cps = 35
while True:
    if kb.is_pressed('y') == True:
        for x in range(cps) :
            gui.press('u')
            t.sleep(1 / cps)