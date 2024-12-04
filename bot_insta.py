import pyautogui
import pyperclip
from time import sleep

email = pyautogui.prompt(text="Digite seu email", title="Dadosde Login")
senha = pyautogui.password(text='Digite sua senha', title="Dadosde Login", mask='*' )

pyautogui.click(1000,200,duration=0.5)

pyautogui.typewrite(email)
pyautogui.press('enter')
pyautogui.typewrite(senha)