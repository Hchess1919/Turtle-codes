import turtle as t

t.bgcolor('black')
t.speed(0)

color=['green','red','blue','yellow']

for i in range(50):
    t.circle(1*i)
    t.circle(-1*i)
    t.left(i)
    t.color(color[i%4])
t.done()