import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(rpaddle.up, "Up")
screen.onkey(rpaddle.down, "Down")
screen.onkey(lpaddle.up, "w")
screen.onkey(lpaddle.down, "s")

play = True
while play:
    screen.update()
    time.sleep(0.1)
    ball.move()

screen.exitonclick()