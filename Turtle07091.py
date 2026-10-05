from
color (255)
shape('turtle') ## вид черепаха
speed() ## скорость рисования

r = 255
g = 255
b = 0
br = 0
bg = 255
bb = 0
color = ((br,bg,bb), (r,g,b))
pensize (4)

for i in range(150,10,-25):
     fillcolor((r,g,b))
     for j in range
        begin_fill()
        circle(j)
        end_fill()
        rt(45)
    r -= 30
    g -= 15
    b += 30

    br += 15
    bg -= 15
    bb += 30
mainloop()