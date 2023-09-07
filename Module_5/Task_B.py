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
    t.speed(0)
    t.forward(random.randrange(0, 25))
    angle = t.heading()
    t.left(random.randrange(angle-45, angle+45))


# def print_close():
#     # turtle.hideturtle()
#     turtle.color("green")
#     turtle.write("Close")

rectangle(-200, -200, 500, 500, "lightblue")

t1_x = random.randrange(-200, 300)
t1_y = random.randrange(-200, 300)
t2_x = random.randrange(-200, 300)
t2_y = random.randrange(-200, 300)


t1 = make_turtle(t1_x,
                 t1_y, 'red')
t2 = make_turtle(t2_x,
                 t2_y, 'green')


count = 0
for i in range(500):
    move_random(t1)
    move_random(t2)

    x_diff = t1_x-t2_x
    y_diff = t1_y-t2_y
    if abs(x_diff) <= 50 and abs(y_diff) <= 50:

        t1.write("Close")
        count += 1


print('count is', count)
turtle.done()
