from turtle import Turtle as t, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Make your bet", "Which turtle will win? Enter a colour: ")
colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
all_turtles = []

for timmy_index in range(0, 6):
    new_turtle = t(shape="turtle")
    new_turtle.color(colours[timmy_index])
    new_turtle.up()
    new_turtle.goto(x=-230, y=-100 + (timmy_index * 40))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You won!")
            else:
                print(f"You lost! The winning turtle was {winning_turtle}")

        random_distance = random.randint(0,10)
        turtle.fd(random_distance)


screen.exitonclick()