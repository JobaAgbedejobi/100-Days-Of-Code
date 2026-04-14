from turtle import Turtle as t, Screen
import random
timmy = t()
screen = Screen()
screen.colormode(255)
timmy.shape("turtle")
timmy.color("darkmagenta")
timmy.speed("fastest")
timmy.ht()
colour_list = [(237, 221, 110), (19, 110, 193), (224, 61, 94), (226, 151, 89), (119, 153, 209), (216, 127, 162), (143, 89, 46), (33, 196, 118), (149, 179, 16), (103, 106, 195), (200, 13, 34), (233, 57, 46), (242, 154, 185), (113, 193, 149), (189, 48, 82), (17, 183, 210), (145, 225, 173), (34, 52, 118), (134, 217, 235), (234, 172, 157), (197, 214, 5), (33, 37, 80), (8, 156, 117), (172, 176, 227), (86, 30, 34), (83, 33, 31), (254, 4, 46), (202, 18, 14), (67, 74, 47)]


def dash():
    timmy.setheading(0)
    colour = random.choice(colour_list)
    timmy.dot(20, (colour))
    timmy.up()
    timmy.fd(50)

def dotted_line():
    for _ in range(10):
        dash()

def reshape():
    timmy.setheading(90)
    timmy.up()
    timmy.fd(50)
    timmy.setx(-220)

def grid():
    timmy.up()
    timmy.goto(-220,-220)
    timmy.down()
    for _ in range(10):
        dotted_line()
        reshape()

grid()
screen.exitonclick()
