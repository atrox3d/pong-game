from turtle import Turtle

PADDLESTEP = 30


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        self.sety(self.ycor() + PADDLESTEP)

    def down(self):
        self.sety(self.ycor() - PADDLESTEP)
