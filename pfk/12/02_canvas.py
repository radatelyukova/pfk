#!/usr/bin/env python3
################################################################################
#   02_canvas.py
#
#   <Executable Module Purpose>
#
#   22.07.2017  Created by:  rada
################################################################################

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width = 500, height = 500, bg = 'red')
canvas.pack()

canvas.create_line(0, 0, 500, 500)
canvas.create_rectangle(100, 100, 200, 400)
canvas.create_line(400, 100, 200, 300)
canvas.create_rectangle(400, 100, 200, 300)

tk.mainloop()