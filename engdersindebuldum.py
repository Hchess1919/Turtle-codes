import turtle as t
import random
import time

siyah='black'
beyaz='white'

t.color(siyah)
# t.window_width(100)
# t.window_height(300)
t.penup()
t.goto(-300,300)
t.pendown()


t.begin_fill()
for a in range(2):
    t.forward(130)
    t.right(90)
    t.forward(500)
    t.right(90)
t.end_fill()
t.done()