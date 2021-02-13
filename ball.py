from turtle import Turtle

BALLSTEP = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.xstep = BALLSTEP
        self.ystep = BALLSTEP

    def move(self):
        x = self.xcor() + self.xstep
        y = self.ycor() + self.ystep

        self.goto(x, y)

    def ybounce(self):
        self.ystep *= -1

    def xbounce(self):
        self.xstep *= -1

    def reset(self):
        self.goto(0, 0)
        self.xbounce()
