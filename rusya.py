import turtle as t
import random
import time

#t.hideturtle()
siyah='black'
beyaz='white'

t.color(beyaz)
t.bgcolor(siyah)
t.penup()
t.goto(-300,300)
t.pendown()


t.begin_fill()
for a in range(2):
    t.forward(550)
    t.right(90)
    t.forward(100)
    t.right(90)
t.right(90)
t.end_fill()


 

t.begin_fill()
t.forward(200)
t.color('blue')
for a in range(2):
    t.left(90)
    t.forward(550)
    t.left(90)
    t.forward(100)
t.end_fill()


t.color('red')
t.forward(100)
t.begin_fill()
for a in range(2):
    t.left(90)
    t.forward(550)
    t.left(90)
    t.forward(100)
t.end_fill()


t.done()