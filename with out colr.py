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
time.sleep(1)
t.bgcolor(siyah)
t.done()