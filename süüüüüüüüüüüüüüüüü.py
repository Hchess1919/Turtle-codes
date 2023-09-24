import turtle
import random




renkler=["red","blue","cyan","green","aliceblue","antiquewhite","antiquewhite1","antiquewhite2","antiquewhite3","antiquewhite4","aqua","aquamarine1","aquamarine2","aquamarine3","aquamarine4","azure","azure1","azure2","azure3","azure4","blue4","beige","bisque1","bisque2","bisque3","bisque4",]
i=0
t = turtle.Turtle()
t.speed(i)

while True:
    color=random.choice(renkler)
    t.color(color)
    t.forward(i)
    i+=1
    t.left(160)