from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.up()
        self.score = 1
        self.goto(-290,270)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def next_level(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over!", align="center", font=FONT)
