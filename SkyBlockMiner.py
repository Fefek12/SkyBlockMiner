import pyautogui
from time import sleep

print('Witaj w SkyBlockMiner!\nWybierz opcję naciskając liczbę i Enter.')
choose = input("1 Włącz automatyczne kopanie (kopiesz w miejscu)\n2 Włącz automatyczne kopanie z Anty-AFK (kopisz, ale ruszasz się na lewo i prawo)\n>> ")

if choose == '2':

    print("Właśnie działa! Masz 5 sekund by przejść do Minecrafta!")

    sleep(5)

    pyautogui.mouseDown(button='left')

    while True:
        pyautogui.keyDown('a')
        sleep(1)
        pyautogui.keyUp('a')
        sleep(1)
        pyautogui.keyDown('d')
        sleep(1)
        pyautogui.keyUp('d')
elif choose == '1':

    print("Właśnie działa! Masz 5 sekund by przejść do Minecrafta!")

    sleep(5)

    pyautogui.mouseDown(button='left')