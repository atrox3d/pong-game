import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RPADDLE_POSITION = 350, 0
LPADDLE_POSITION = -350, 0

BALL_WIDTH = 20
BALL_HEIGHT = 20

WALL_CENTER_DISTANCE = (SCREEN_HEIGHT / 2)
WALL_BALL_LIMIT = WALL_CENTER_DISTANCE - (BALL_HEIGHT / 2)
NORTH_WALL = WALL_BALL_LIMIT
SOUTH_WALL = WALL_BALL_LIMIT * -1


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


rpaddle = Paddle(RPADDLE_POSITION)
lpaddle = Paddle(LPADDLE_POSITION)
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
    #
    #   wall collision
    #
    if ball.ycor() >= NORTH_WALL:
        ball.ybounce()
    elif ball.ycor() <= SOUTH_WALL:
        ball.ybounce()
    #
    #   rpaddle collision
    #

screen.exitonclick()