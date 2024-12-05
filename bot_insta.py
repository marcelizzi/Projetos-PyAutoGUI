import pyautogui
import webbrowser
from time import sleep

#login e senha pre cadastrados
login = "admin"
senha = "123deoliveira4"

# opcao de solicitar login e senha ao usuario
# login = pyautogui.prompt(text="Digite seu telefonne, nome de usuário ou email", title="Dados de Login")
# senha = pyautogui.password(text='Digite sua senha', title="Dados de Login", mask='*' )

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

#loop diario
while True:
    webbrowser.open('https://www.instagram.com/nike', new=1, autoraise=True)
    sleep(5)
    pyautogui.click(480, 650, duration=1)
    sleep(1)
    try:
        pyautogui.locateCenterOnScreen('fullheart.PNG', confidence=0.9)
        #postagem ja curtida,  fechar aba
        pyautogui.hotkey('ctrl', 'w')
    except pyautogui.ImageNotFoundException:
        pyautogui.click(690, 570, duration=1)
        sleep(1)
        pyautogui.click(870, 680, duration=1)
        pyautogui.typewrite("Nice")
        sleep(1)
        pyautogui.click(1130, 675, duration=1)
        sleep(1)
        #tarefa executada, fechar aba. pensei em implementar com F5, mas optei  por essa versão pq diminuiu meu trabalho nos testes
        pyautogui.hotkey('ctrl', 'w')
    sleep(86400)
