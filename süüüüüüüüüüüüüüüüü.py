import turtle
import random
turtle.bgcolor("black")



renkler=["red","blue","cyan","green","aliceblue","aqua","aquamarine1","aquamarine2","aquamarine3","aquamarine4","azure","azure1","azure2","azure3","azure4","blue4","beige","bisque1","bisque2","bisque3","bisque4",]
i=0
t = turtle.Turtle()
t.speed(i)

while True:
    colors=random.choice(renkler)
    t.color(colors)
    t.forward(i)
    i+=1
    t.left(i)