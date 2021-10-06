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
    direction = [0, 90, 180, 270]
    for i in range(10000):
        color = generate_color()
        turt.pencolor(color)
        turt.right(random.choice(direction))
        turt.forward(50)

walk()

screen.exitonclick()
