import pyautogui
from time import sleep
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import webbrowser

#Window
window = tk.Tk()
window.geometry('400x300')
window.title('SkyBlockMiner')
window.iconbitmap('Z:\SkyBlockMiner\Gui App\.assets\SkyBlockMinerIcon.ico')

#Program varibles
eatingOn = False
antiAFkOn = False
autoSellOn = False

isItOn = False
command = tk.StringVar()
chatKey = tk.StringVar()

#Program menu functions
def info():
    infoWindow = tk.Tk()
    infoWindow.geometry("500x100")
    infoWindow.title("Info")

    ttk.Label(infoWindow, text=" ").pack()
    ttk.Label(infoWindow, text=" ").pack()
    ttk.Label(infoWindow, text='Version 3 BETA').pack()

    infoWindow.mainloop()

def author():
    authorWindow = tk.Tk()
    authorWindow.geometry("500x100")
    authorWindow.title("Author")

    ttk.Label(authorWindow, text=" ").pack()
    ttk.Label(authorWindow, text=" ").pack()
    ttk.Label(authorWindow, text='Fefek').pack()

    authorWindow.mainloop()

def discord():
    def joinDiscord():
        webbrowser.open('https://discord.gg/Fypw4WPYGe')
    
    discordWindow = tk.Tk()
    discordWindow.geometry("500x150")
    discordWindow.title("Discord")

    ttk.Label(discordWindow, text=" ").pack()
    ttk.Label(discordWindow, text=" ").pack()
    ttk.Label(discordWindow, text='Discord link: https://discord.gg/Fypw4WPYGe').pack()
    ttk.Button(discordWindow, text="Join", command=joinDiscord).pack()

    discordWindow.mainloop()

#Program menu
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Info", command=info)
filemenu.add_command(label="Author", command=author)
filemenu.add_command(label="Discord", command=discord)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Program", menu=filemenu)
menubar.add_cascade(label="Exit", command=window.quit)

#OFF and ON button functions
def antiAFKFuncOn():
    global antiAFkOn
    antiAFkOn = True
def antiAFKFuncOff():
    global antiAFkOn
    antiAFkOn = False

def autoSellFuncOn():
    global autoSellOn
    autoSellOn = True
def autoSellFuncOff():
    global autoSellOn
    autoSellOn = False

#Program functions
def startMining():
    global isItOn

    if antiAFkOn == True:

        if autoSellOn == True:
            if isItOn == True:
                messagebox.showinfo('Info', "You have five seconds to open Minecraft!")

                sellTime = 600
                sleep(5)

                pyautogui.mouseDown(button='left')

                while True:
                    pyautogui.keyDown('a')
                    sleep(1)
                    sellTime = sellTime - 1
                    pyautogui.keyUp('a')
                    sleep(1)
                    sellTime = sellTime - 1
                    pyautogui.keyDown('d')
                    sleep(1)
                    sellTime = sellTime - 1
                    pyautogui.keyUp('d')

                    if sellTime <= 0:
                        pyautogui.mouseUp(button='left')
                        pyautogui.press(chatKey.get())
                        pyautogui.write(command.get())
                        pyautogui.press('Enter')
                        pyautogui.press("Esc")
                        pyautogui.mouseDown(button='left')

                        sellTime = 600
            else:
                messagebox.showinfo('Info', "Set autosell command")

                isItOn = True

                ttk.Label(window, text="Auto sell command").grid(row=4, column=0)
                ttk.Entry(window, textvariable=command).grid(row=4, column=1)

                ttk.Label(window, text="Chat button").grid(row=5, column=0)
                ttk.Entry(window, textvariable=chatKey).grid(row=5, column=1)

        else:
            messagebox.showinfo('Info', "You have five seconds to open Minecraft!")
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

    else:
        if autoSellOn == True:
            if isItOn == True:
                messagebox.showinfo('Info', "You have five seconds to open Minecraft!")
                sellTime = 600
                sleep(5)

                pyautogui.mouseDown(button='left')

                while True:
                    sleep(1)
                    sellTime = sellTime - 1

                    if sellTime <= 0:
                        pyautogui.mouseUp(button='left')
                        pyautogui.press(chatKey.get())
                        pyautogui.write(command.get())
                        pyautogui.press("Enter")
                        pyautogui("Esc")
                        pyautogui.mouseDown(button='left')

                        sellTime = 600
            else:
                messagebox.showinfo('Info', "Set autosell command")

                isItOn = True

                ttk.Label(window, text="Auto sell command").grid(row=4, column=0)
                ttk.Entry(window, textvariable=command).grid(row=4, column=1)

                ttk.Label(window, text="Chat button").grid(row=5, column=0)
                ttk.Entry(window, textvariable=chatKey).grid(row=5, column=1)

        else:
            messagebox.showinfo('Info', "You have five seconds to open Minecraft!")
            sleep(5)

            pyautogui.mouseDown(button='left')

#Window elements
ttk.Label(window, text='Anti-AFK function').grid(row=1, column=0)
ttk.Button(window, text='OFF', command=antiAFKFuncOff).grid(row=1, column=1)
ttk.Button(window, text='ON', command=antiAFKFuncOn).grid(row=1, column=2)

ttk.Label(window, text='Auto sell').grid(row=2, column=0)
ttk.Button(window, text='OFF', command=autoSellFuncOff).grid(row=2, column=1)
ttk.Button(window, text='ON', command=autoSellFuncOn).grid(row=2, column=2)

ttk.Label(window, text=' ').grid(row=3, column=0) 

ttk.Label(window, text=' ').grid()
ttk.Label(window, text=' ').grid()
ttk.Label(window, text=' ').grid()
ttk.Label(window, text=' ').grid()
ttk.Button(window, text='Start mining', command=startMining).grid()

window.config(menu=menubar)
window.mainloop()