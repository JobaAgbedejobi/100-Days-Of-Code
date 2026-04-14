from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):


    def __init__(self):
        super().__init__()
        self.ht()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.up()
            new_car.speed(self.car_speed)
            y_cor = random.randint(-250, 250)
            new_car.goto(300, y_cor)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.bk(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT