import pyautogui
from time import sleep

with open ("partesap.txt", "r") as arquivo:
    for linha in arquivo:
        valores = linha.strip().split(',')
        uni = valores[0]
        # pyautogui.click(1757,768, duration=1)
        # pyautogui.write(uni + '  PART ORIGINAL\n')
        del valores[0]
        for valor in valores:
            pyautogui.click(78,267, duration=1)
            pyautogui.write(uni)
            pyautogui.click(161,449, duration=1)
            pyautogui.moveTo(299,450, duration=1)
            pyautogui.click(314,552, duration=1)

            pyautogui.press('backspace')
            pyautogui.click(934,567, duration=1)
            pyautogui.write(valor)
            pyautogui.click(998,653, duration=1)
            pyautogui.click(283,268, duration=1)

        
        print('linha processada')