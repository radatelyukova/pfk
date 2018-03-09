#!/usr/bin/env python3
# coding: utf-8
################################################################################
#   01_button.py
#
#   <Executable Module Purpose>
#
#   22.07.2017  Created by:  rada
################################################################################

from tkinter import *

def say_hello():
    print('Я родился! Уху')

tk = Tk()
btn = Button(tk, text = "click me", command = say_hello)
btn.pack()

tk.mainloop()