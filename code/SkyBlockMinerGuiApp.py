import pyautogui
from time import sleep
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('300x300')
window.title('SkyBlockMiner')


def function2():
    ttk.Label(window, text="Uwaga! Ta funkcja jest zakazana na niektórych serwerach!").pack()
    ttk.Label(window, text="Uwaga! Ta funkcja jest bardzo awaryjna!").pack()
    ttk.Label(window, text="Kliknij dowolny przycisk by zakończyć działanie programu").pack()

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


def function1():
    ttk.Label(window, text="Kliknij dowolny przycisk by zakończyć działanie programu").pack()

    sleep(5)

    pyautogui.mouseDown(button='left')


def info():
    infoWindow = tk.Tk()
    infoWindow.geometry("500x100")
    infoWindow.title("Info")

    ttk.Label(infoWindow, text='Po uruchomieniu programu masz 5 sekund by przejść do MC').pack()
    ttk.Label(infoWindow, text='Wersja 1.0').pack()

    infoWindow.mainloop()


ttk.Button(window, text="Rozpocznij kopanie", command=function1).pack()
ttk.Button(window, text="Rozpocznij kopanie z funkcją anty-AFK", command=function2).pack()
ttk.Button(window, text="Info", command=info).pack()

window.mainloop()
