#By: Binazir Biglari
#Creating 2 turtles and moving them

import turtle
n = input("what is the window screen ? ")
m = input("whatis the alex color ? ")

wn = turtle.Screen()
wn.bgcolor(n)
wn.title("Two Turtles")
alex = turtle.Turtle()
alex.color(m)
tess = turtle.Turtle()

tess.color('red')
tess.forward(20)

wn.mainloop()
