#This just finds the coordinates on the mouse. Just used it to assist in finding coordinates
import pyautogui as gui
import time as t
loop = 3

while loop > 0:
    t.sleep(1)
    print(gui.position())
    loop -= 1
