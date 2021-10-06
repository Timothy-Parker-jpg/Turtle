from turtle import Turtle, Screen

turt = Turtle()
turt.shape("turtle")

def triangle():
    turt.color("green")
    for i in range(3):
        turt.forward(100)
        turt.right(120)
def square():
    turt.color("purple")
    for i in range(4):
        turt.forward(100)
        turt.right(90)
def pentagon():
    turt.color("blue")
    for i in range(5):
        turt.forward(100)
        turt.right(72)

def hexagon():
    turt.color("orange")
    for i in range(6):
        turt.forward(100)
        turt.right(360/6)

def heptagon():
    turt.color("brown")
    for i in range(7):
        turt.forward(100)
        turt.right(360 / 7)

def octagon():
    turt.color("violet")
    for i in range(8):
        turt.forward(100)
        turt.right(360 / 8)

def nonagon():
    turt.color("red")
    for i in range(9):
        turt.forward(100)
        turt.right(360 / 9)

def decagon():
    turt.color("gray")
    for i in range(10):
        turt.forward(100)
        turt.right(360 / 10)


triangle()

square()

pentagon()

hexagon()

heptagon()

octagon()

nonagon()

decagon()

screen = Screen()

screen.exitonclick()
