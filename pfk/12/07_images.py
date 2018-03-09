#!/usr/bin/env python3
################################################################################
#   07_images.py
#
#   NB! pip3 install Pillow
#
#   04.03.2018  Created by:  rada
################################################################################

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width = 1000, height = 500, bg = 'cyan')
canvas.pack()

# For GIF only
my_image = PhotoImage(file = 'pic.gif')
canvas.create_image(10, 10, anchor = NW, image = my_image)

# Other image formats
from PIL import Image, ImageTk

img = Image.open('T.png')
img.show()

img_t = Image.open('/Users/rada/Desktop/turtle.png')
img_t.show()

tk.mainloop()