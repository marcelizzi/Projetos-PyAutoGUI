import pyautogui
import pyperclip
import webbrowser
from time import sleep

#solicitando login e senha do usuario
login = pyautogui.prompt(text="Digite seu telefonne, nome de usuário ou email", title="Dados de Login")
senha = pyautogui.password(text='Digite sua senha', title="Dados de Login", mask='*' )

login = "easy.3dprint"
senha = "F9ufv%%Iinsta"
sleep(3)
webbrowser.open('https://www.instagram.com/', new=1, autoraise=True)
sleep(3)
pyautogui.press('tab')
sleep(1)
pyautogui.press('tab')
sleep(1)
pyautogui.typewrite(login)
sleep(1)
pyautogui.press('tab')
pyautogui.typewrite(senha)
sleep(1)
pyautogui.click(pyautogui.locateCenterOnScreen('login.PNG'), duration=1)
sleep(5)
webbrowser.open('https://www.instagram.com/nike', new=1, autoraise=True)
sleep(5)
pyautogui.click(485,695,duration=1)

position = pyautogui.locateCenterOnScreen('emptyheart.PNG')
print(position)
