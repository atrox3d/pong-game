from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(350, 0)

    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)