import pyautogui
import time

#No cmd use pyautogui.position() para descobrir a posiçao do mouse 

#Faz o cursor do mouse ir até a posição e realiza o click
pyautogui.moveTo(70,741, duration = 0.7)
pyautogui.click()

#Vai abrir a caixa de texto, eu ensiro a palavra e depois pressiono enter
pyautogui.typewrite('cmd', interval = 0.9)#velocidade de digitação
pyautogui.press('enter')#precisa tecla do teclado
time.sleep(2)

#Fecha cmd
pyautogui.moveTo(444,242, duration = 0.7)
pyautogui.click()
pyautogui.typewrite('exit', interval = 0.3)
pyautogui.press('enter')