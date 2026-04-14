import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    car_manager.move_cars()
    time.sleep(0.1)
    screen.update()

#Generate a new car
    car_manager.generate_car()

#Detect collision with obstacle
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

#Detect when you've reached the finish line
    if player.level_completed():
        player.goto(STARTING_POSITION)
        car_manager.increase_speed()
        scoreboard.next_level()

screen.exitonclick()