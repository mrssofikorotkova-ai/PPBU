import turtlrwer___ as t
t.ht()
t.pensize(5)
for r in range(40, 0, -10):
    for i in range(6):
        t.color(255, 165, r * 6)
        t.fillcolor(162, r * 6, 255)
        t.begin_fill()
        t.square(r)
        t.end_fill()
        t.rt(60)