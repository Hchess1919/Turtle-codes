import turtle
import random


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    turtle.color(R, G, B)

def turn_and_change_color(x, y):
    turtle.left(10)
    change_color()

turtle.onscreenclick(turn_and_change_color)

def move_forward():
    turtle.forward(1)
    turtle.ontimer(move_forward, 25)

move_forward()

turtle.mainloop()