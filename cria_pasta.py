#importando PyAutoGUI
import pyautogui

#importando Time
from time import sleep

pyautogui.rightClick(940,400)
pyautogui.moveTo(980,660,duration=2)
sleep(0.5)
pyautogui.moveTo(855,660,duration=1)
pyautogui.leftClick(855,530,duration=2)