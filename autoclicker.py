import time
import tkinter as tk
import pyautogui as pag

top = tk.Tk()

#sort out stuff like title n stuff and resize
top.geometry('180x200')
top.resizable(False, False)
top.title('ac')
#text
l = tk.Label(top, text = "Input clicks")
l.config(font =("Courier", 8))
l.place(x=90, y=15)

#clcik stuff
click_value = tk.StringVar()
a = tk.Spinbox(top, from_=0, to=100, textvariable=click_value)
a.place(x=95, y = 0)

#very important this make fastt
pag.PAUSE = 0

#start the impotatnt
def startClick():
   time.sleep(3)
   for x in range (int(click_value.get())):
       pag.click()

#buttinsss
w = tk.Button(top, text= "click", command=startClick)
w.place(x=75, y=100)

#text
l = tk.Label(top, text = "Start clicking.")
l.config(font =("Courier", 8))
l.place(x=35, y=125)

#text aghain
l = tk.Label(top, text = "(3 Second Delay)")
l.config(font =("Courier", 8))
l.place(x=30, y=150)

#end of gui
top.mainloop()