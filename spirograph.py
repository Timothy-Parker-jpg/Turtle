from turtle import Turtle, Screen
import random


def generate_color():
    color = []
    for i in range(3):
        color.append(random.randint(0, 255))
    return color



turt = Turtle()
turt.speed(100)
turt.shape("turtle")
turt.shapesize(1, 1)
screen = Screen()
screen.colormode(255)


for i in range(90):
    turt.pencolor(generate_color())
    turt.circle(100)
    turt.right(4)








screen.exitonclick()