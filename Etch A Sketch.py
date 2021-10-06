import random
from turtle import Turtle, Screen

turt = Turtle()
turt.pensize(15)
turt.speed(10)
turt.shape("turtle")
turt.shapesize(1.5, 1.5)
screen = Screen()
screen.colormode(255)


def generate_color():
    color = []
    for i in range(3):
        color.append(random.randint(0, 255))
    return color


def walk():
    turt.pencolor(generate_color())
    turt.fd(25)


def right_turn():
    turt.right(25)


def left_turn():
    turt.left(25)


def back_walk():
    turt.back(25)


def clear():
    turt.clear()


def cont(func):
    cond = True
    while cond:
        func
        if screen.onkeyrelease(None, "Up"):
            cond = False


screen.onkey(walk, "Up")
screen.onkey(clear, "c")
screen.onkey(right_turn, "Right")
screen.onkey(left_turn, "Left")
screen.onkey(back_walk, "Down")
screen.listen()


screen.exitonclick()
