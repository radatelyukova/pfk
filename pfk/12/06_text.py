#!/usr/bin/env python3
################################################################################
#   06_text.py
#
#   <Executable Module Purpose>
#
#   11.03.2018  Created by:  rada
################################################################################

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width = 1400, height = 800, bg = 'cyan')
canvas.pack()

#canvas.create_text(150, 100, text='My dady is POOP!!!')

canvas.create_text(200, 200, text = 'My mommy is COOL!!!')
canvas.create_text(200, 400, text = 'My mommy is COOL!!!', font = ('Times', 20), fill='white')

tk.mainloop()