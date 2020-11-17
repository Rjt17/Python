#!/usr/bin/env python
print('''python is love''')
rajat = "elitem"
print ("rajat is " "elitem")
print('''"whats" your name\'''')
print(R"what\'s your name?")
print(format('"hello"','^15'))
import tkinter
print(tkinter.TkVersion)
from tkinter import Tk
root = Tk()
root.geometry("400x200+150+150")
#screen.width = root.winfo_screenmmwidth()
screen_height = root.winfo_screenheight()
#print("screen width:",screenmwidth)
print("screen height:",screen_height)
#root.attributes('-fullscreen', True)
root.title("fun with python")
root.mainloop()