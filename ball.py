from turtle import Turtle

BALLSTEP = 10
MOVESPEED = 0.08


class Ball(Turtle):

    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.xstep = BALLSTEP
        self.ystep = BALLSTEP
        self.move_speed = MOVESPEED

    def move(self):
        x = self.xcor() + self.xstep
        y = self.ycor() + self.ystep

        self.goto(x, y)

    def ybounce(self):
        self.ystep *= -1

    def xbounce(self):
        self.xstep *= -1
        self.move_speed *= 0.9
        print(f"speedup: SLEEP_TIME = {self.move_speed}")

    def reset(self):
        self.goto(0, 0)
        self.xbounce()
        self.move_speed = MOVESPEED
        print(f"speedup: SLEEP_TIME = {self.move_speed}")

    def speedup(self):
        if self.move_speed - 0.01 > 0.0:
            self.move_speed -= 0.01
            print(f"speedup: SLEEP_TIME = {self.move_speed}")
        else:
            print(f"speedup: MIN REACH SLEEP_TIME = {self.move_speed}")

    def speeddown(self):
        self.move_speed += 0.01
        print(f"speeddown: SLEEP_TIME = {self.move_speed}")
