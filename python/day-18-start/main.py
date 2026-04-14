from turtle import Turtle as t, Screen
import random

timmy = t()
screen = Screen()
screen.colormode(255)
timmy.shape("turtle")
timmy.color("darkmagenta")

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

#CHALLENGE 5
timmy.speed("fastest")
def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
        timmy.color(random_colour())

spirograph(10)
screen.exitonclick()
