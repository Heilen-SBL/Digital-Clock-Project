from Tkinter import Tk
from Tkinter import Label
import time
import sys

#Window

master = Tk()
master.title("Digital Clock")

hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"

#Function

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,get_time)

#Labels

clock = Label(master, font=("Calibri",90),bg="black",fg="grey")
clock.pack()

get_time()

master.mainloop()