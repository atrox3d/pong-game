from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.xstep = 10
        self.ystep = 10

    def move(self):
        x = self.xcor() + self.xstep
        y = self.ycor() + self.ystep

        self.goto(x, y)

    def bounce(self):
        self.ystep *= -1
