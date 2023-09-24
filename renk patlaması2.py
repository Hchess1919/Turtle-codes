import turtle
import random
turtle.bgcolor("black")



renkler=["red","blue","cyan","green","yellow"]
i=1
t = turtle.Turtle()
t.speed(0)

while i!=180:
    colors=random.choice(renkler)
    t.color(colors)
    t.forward(i)
    i+=1
    t.left(i)
    
input()