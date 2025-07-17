import pyautogui
from time import sleep

# 1 - Clicar e digitar meu usuario
pyautogui.click(978,546, duration=2)
pyautogui.write('war')

# 2 - clicar e digitar minha senha
pyautogui.click(977,574, duration=2)
pyautogui.write('123')

# 3 - clicar em "ENTRAR" 
pyautogui.click(848,615, duration=2)

# 4 - extrair cada produto
with open('test.avl','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        #4.1 - clicar e digitar produto
        pyautogui.click(640,525, duration=2)
        pyautogui.write(produto)

        #4.2 - clicar e digitar quantidadewar
        pyautogui.click(635,558, duration=2)
        pyautogui.write(quantidade)

        #4.1 - clicar e digitar preçowar
        #pyautogui.click(634,594, duration=2)123war
        #pyautogui.write(preco)

        #4.1 - clicar em registrarProduto 
        pyautogui.click(500,791, duration=1)
        sleep(1)