import turtle
import random


def make_turtle(x, y, color):
    t = turtle.Turtle()
    jump(t, x, y)
    t.color(color)
    return t


def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def rectangle(x, y, width, height, color):
    t = make_turtle(x, y, color)
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.speed(0)
        t.forward(dist)
        t.left(90)
    t.end_fill()

# random move of the toad


def move_random(t):
    t.forward(random.randrange(0, 25))
    t.left(random.randrange(-45, 45))


rectangle(-200, -200, 500, 500, "lightblue")
t1 = make_turtle(random.randrange(-200, 300),
                 random.randrange(-200, 300), 'red')
t2 = make_turtle(random.randrange(-200, 300),
                 random.randrange(-200, 300), 'green')
for i in range(250):
    move_random(t1)
    move_random(t2)


turtle.done()
