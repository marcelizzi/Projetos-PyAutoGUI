import webbrowser
import pyautogui
from time import sleep

webbrowser.open('https://cursoautomacao.netlify.app/', new=1, autoraise=True)
sleep(2)
pyautogui.hotkey('ctrl','f')
pyautogui.typewrite('Exemplos Alertas')
pyautogui.press('esc')
pyautogui.click(1035,450,duration=1)
pyautogui.typewrite('Marcel')
pyautogui.click(1060,480,duration=1)
pyautogui.click(855,190,duration=1)
#pyautogui.click(955,105,duration=1)
pyautogui.press('home')
pyautogui.hotkey('ctrl','f')
pyautogui.typewrite('Planilha Excel')
pyautogui.press('esc')
#pyautogui.click(955,105,duration=1)
pyautogui.click(195,450,duration=1)
pyautogui.click(390,450,duration=1)
pyautogui.alert(text='Você Terminou', title='Alerta',button='OK')
Marcel