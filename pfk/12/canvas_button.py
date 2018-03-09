#!/usr/bin/env python3
################################################################################
#   canvas_button.py
#
#   <Executable Module Purpose>
#
#   21.02.2018  Created by:  rada
################################################################################

from tkinter import *

tk = Tk()

canv = Canvas(tk, width = 800, height = 400, bg = 'lightgreen', cursor="pencil")
canv.pack()

def dummy():
    print('Я мишка Гомми Бэр!!!!!!!!!!!!!')

btn = Button(tk, text = 'Push me!', command = dummy)
btn.pack()

canv.create_rectangle(400, 100, 200, 300)

tk.mainloop()