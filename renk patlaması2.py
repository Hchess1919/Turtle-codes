import turtle
import random
turtle.bgcolor("black")



renkler=["red","blue","cyan","green","yellow"]
i=1
t = turtle.Turtle()
t.speed(i/100)

while i!=180:
    colors=random.choice(renkler)
    t.color(colors)
    t.forward(i)
    i+=10
    t.left(i)
    
input()