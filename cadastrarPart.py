import pyautogui
from time import sleep

# 4 - extrair cada produto
with open('test2.avl','r') as arquivo:
    for linha in arquivo:
        produto = linha

        file = arquivo.read().replace(",", "\n")
        
        pyautogui.click(1824,821, duration=0.1)
        pyautogui.write(produto)

        sleep(0.3)