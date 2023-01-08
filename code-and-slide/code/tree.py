# Draws a tree recursivly
#By: Binazir Biglari

from turtle import *
from math import *


def line(x, y, x2, y2):
    ''' Draw a line from (x, y) to (x2, y2) '''
    penup()
    goto(x, y)
    pendown()
    goto(x2, y2)


def draw_tree(x, y, size, angle, width):
    ''' Draw a tree of given size and angle at (x, y) '''
    if size < 4:
        return
    x2 = x + size * cos(radians(angle))
    y2 = y + size * sin(radians(angle))
    pensize(max(width, 1))
    line(x, y, x2, y2)
    draw_tree(x2, y2, size * 0.75, angle + 30, width * 0.80)
    draw_tree(x2, y2, size * 0.57, angle - 50, width * 0.73)


# main program
speed(10)
delay(2)
draw_tree(0, 0, 80, 90, 8)
mainloop()
