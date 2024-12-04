#importando PyAutoGUI
import pyautogui

#importando Time
from time import sleep

pyautogui.moveTo(1183,402,duration=0.1)
pyautogui.dragTo(733,201, duration=1, button='left')
pyautogui.move(30,30,duration=0.1)
pyautogui.dragTo(766,683,duration=0.5, button='left')