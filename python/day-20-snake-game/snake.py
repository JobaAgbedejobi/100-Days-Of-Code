from turtle import Turtle as t

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = t("square")
        segment.color("white")
        segment.up()
        segment.goto(position)
        self.snake.append(segment)

    def extend_segment(self):
        self.add_segment(self.snake[-1].position())

    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        for snake_segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_segment - 1].xcor()
            new_y = self.snake[snake_segment - 1].ycor()
            self.snake[snake_segment].goto(x=new_x, y=new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
