import  pyautogui


checkbox_position = pyautogui.locateCenterOnScreen('checkbox.png')  
pyautogui.click(checkbox_position,duration=2.5)