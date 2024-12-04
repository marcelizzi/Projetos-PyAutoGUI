import pyautogui
import pyperclip

def escreve_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

pyautogui.click(900,350,duration=0.5)
escreve_frase('Automação é Incrível!!!')