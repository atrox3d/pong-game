from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.ystep = -10

    def move(self):
        if self.ycor() >= 300 - 10:
            self.ystep = -10
        elif self.ycor() <= -300 + 10:
            self.ystep = 10

        x = self.xcor() + 10
        y = self.ycor() + self.ystep

        self.goto(x, y)