import turtle
import random
turtle.bgcolor("black")



renkler=["red","blue","cyan","green","yellow"]
i=0
t = turtle.Turtle()
t.speed(i)

while True:
    colors=random.choice(renkler)
    t.color(colors)
    t.forward(i)
    i+=1
    t.left(i)
    
   