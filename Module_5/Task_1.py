import turtle


def make_turtle(x, y):
    t = turtle.Turtle()
    jump(t, x, y)
    return t


def rectangle(x, y, width, height, color):
    t = make_turtle(x, y)
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.speed(0)
        t.forward(dist)
        t.left(90)
    t.end_fill()


def tricolore(x, y, h):
    w = h/2  # färgfältens bredd
    rectangle(x, y, w, h, 'blue')
    rectangle(x+w, y, w, h, 'white')
    rectangle(x+2*w, y, w, h, 'red')


def pentagram(x, y, side):
    t = make_turtle(x, y)
    t.hideturtle()
    t.setheading(270 - 36/2)
    t.fillcolor('green')
    t.begin_fill()
    for i in range(5):
        t.speed(0)
        t.forward(side)
        t.left(180-36)
    t.end_fill()


def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


tricolore(-100, -100, 200)

t = turtle.Turtle()
t.hideturtle()

t.color('green')
for i in range(10):

    if i < 5:

        pentagram(-150 + i*100, -150, 100)
    else:

        pentagram(-650 + i*100, 250, 100)
t.end_fill()

turtle.done()
