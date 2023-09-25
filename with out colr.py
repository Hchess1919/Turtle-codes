import turtle as t
import random
import time

t.speed(0)
renkler=['blue','red','yellow','green','cyan']
i=0
siyah='black'
beyaz='white'

while i!=120:
    color=random.choice(renkler)
    t.bgcolor(color)
    t.color(color)
    i+=1
    t.forward(i)
    t.right(89)
    #time.sleep(1)
t.penup()
t.goto(-40,-300)
t.pendown()
t.color(siyah)
t.write('FINALY RESULT')


time.sleep(1)
t.color(beyaz)
t.write('FINALY RESULT')
t.bgcolor(siyah)
t.done()
