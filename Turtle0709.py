from turtlrwer___ import *
color (255)
shape('turtle') ## вид черепаха
speed() ## скорость рисования

r = 255
g = 255
b = 0
color = ((0,255,0), (r,g,b))
pensize (4)
for i in range(8):
    begin_fill()
    circle(150)
    rt(45)
    end_fill()

