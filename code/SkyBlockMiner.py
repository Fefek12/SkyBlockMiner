import pyautogui
from time import sleep

print('Witaj w SkyBlockMiner')
choose = input('Wybierz opcję:\n1 Kopanie w miejscu\n 2 Kopanie i ruszanie się na lewo i prawo\n3 Info')

if choose == '2':
    print("Program właśnie działa, masz 5 sekund by przejść do Minecrafta!")

    sleep(5)

    print('By zatrzymać program musisz kliknąć dowolny przycisk')

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
    print("Program właśnie działa, masz 5 sekund by przejść do Minecrafta!")
    
    sleep(5)

    pyautogui.mouseDown(button='left')
elif choose == '3':
    print('Wersja 1.0')
