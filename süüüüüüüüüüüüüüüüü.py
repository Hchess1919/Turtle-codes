import turtle
import random



renkler=["red","blue","cyan","green"]
i=0
t = turtle.Turtle()
t.speed(i)

while True:
    color=random.choice(renkler)
    t.color(color)
    t.forward(i)
    i+=1
    t.left(92)