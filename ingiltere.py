import turtle as t
import random
import time

t.penup()
t.goto(70,200)
t.pendown()

for b in range(2):
    t.forward(260)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(350)




t.begin_fill()
t.color('red')
for a in range(2):
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(50)
t.end_fill()

t.penup()
t.goto(330,25)
t.pendown()

t.begin_fill()
t.color('red')
for a in range(2):
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(610)
t.end_fill()



t.done()