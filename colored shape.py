import turtle as t
import random as r
import time 

t.bgcolor('black')

t.speed(0)

i =0
renkler=['blue','red','yellow','green','cyan']
while True:
    i+=1
    color1=r.choice(renkler)
    t.color(color1)
    t.forward(i)
    t.left(89)



    #time.sleep(0.2)
    print('sui')

t.done()