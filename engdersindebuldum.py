import turtle as t
import random
import time

t.hideturtle()
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
    t.forward(200)
    t.right(90)
    t.forward(550)
    t.right(90)



    
t.end_fill()
t.begin_fill()
t.forward(400)
t.color('yellow')
for a in range(2):
    t.right(90)
    t.forward(550)
    t.right(90)
    t.forward(200)
t.end_fill()


t.color('red')
t.forward(200)
t.begin_fill()
for a in range(2):
    t.right(90)
    t.forward(550)
    t.right(90)
    t.forward(200)
t.end_fill()

t.done()