import time
from token import RIGHTSHIFT
from turtle import Screen

from ball import Ball
from paddle import Paddle
#
#   screen
#
from scoreboard import ScoreBoard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#
#   paddles
#
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
RPADDLE_X = 350
LPADDLE_X = -350
RPADDLE_POSITION = RPADDLE_X, 0
LPADDLE_POSITION = LPADDLE_X, 0
#
#   ball
#
BALL_SIZE = 20
HALF_BALL = BALL_SIZE / 2
#
#   upper and lower walls
#
Y_WALL_CENTER_DISTANCE = (SCREEN_HEIGHT / 2)
Y_WALL_BALL_LIMIT = Y_WALL_CENTER_DISTANCE - HALF_BALL
UPPER_WALL = Y_WALL_BALL_LIMIT
LOWER_WALL = Y_WALL_BALL_LIMIT * -1
#
#   left and right wall
#
X_WALL_CENTER_DISTANCE = (SCREEN_WIDTH / 2)
X_WALL_BALL_LIMIT = X_WALL_CENTER_DISTANCE
RIGHT_WALL = X_WALL_BALL_LIMIT
LEFT_WALL = X_WALL_BALL_LIMIT * -1
#
#   collision
#
BALL_PADDLE_COLLISION = 50
RPADDLE_WALL = RPADDLE_X - (PADDLE_WIDTH / 2 )
LPADDLE_WALL = LPADDLE_X - -(PADDLE_WIDTH / 2 )

print(f"SCREEN_WIDTH           : {SCREEN_WIDTH            }")
print(f"SCREEN_HEIGHT          : {SCREEN_HEIGHT           }")
print(f"LPADDLE_POSITION       : {LPADDLE_POSITION        }")
print(f"RPADDLE_POSITION       : {RPADDLE_POSITION        }")
print(f"BALL_SIZE              : {BALL_SIZE               }")
print(f"HALF_BALL              : {HALF_BALL               }")
print(f"Y_WALL_CENTER_DISTANCE : {Y_WALL_CENTER_DISTANCE  }")
print(f"Y_WALL_BALL_LIMIT      : {Y_WALL_BALL_LIMIT       }")
print(f"UPPER_WALL             : {UPPER_WALL              }")
print(f"LOWER_WALL             : {LOWER_WALL              }")
print(f"X_WALL_CENTER_DISTANCE : {X_WALL_CENTER_DISTANCE  }")
print(f"X_WALL_BALL_LIMIT      : {X_WALL_BALL_LIMIT       }")
print(f"RIGHT_WALL             : {RIGHT_WALL              }")
print(f"LEFT_WALL              : {LEFT_WALL               }")
print(f"BALL_PADDLE_COLLISION  : {BALL_PADDLE_COLLISION   }")
print(f"RPADDLE_WALL           : {RPADDLE_WALL            }")
print(f"LPADDLE_WALL           : {LPADDLE_WALL            }")

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


rpaddle = Paddle(RPADDLE_POSITION)
lpaddle = Paddle(LPADDLE_POSITION)
ball = Ball()
print(f"SLEEP_TIME             : {ball.move_speed         }")

scoreboard = ScoreBoard()


def gameover():
    global isgameover
    isgameover = True
    scoreboard.gameover()


screen.listen()
screen.onkeypress(rpaddle.up, "Up")
screen.onkeypress(rpaddle.down, "Down")
screen.onkeypress(ball.speeddown, "Left")
screen.onkeypress(ball.speedup, "Right")
screen.onkeypress(lpaddle.up, "w")
screen.onkeypress(lpaddle.down, "s")

screen.onkeypress(gameover, "Escape")


isgameover = False
while not isgameover:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    #
    #   upper lower wall collision
    #
    if ball.ycor() >= UPPER_WALL:
        ball.ybounce()
    elif ball.ycor() <= LOWER_WALL:
        ball.ybounce()
    #
    #   rpaddle collision
    #
    if ball.distance(rpaddle) < BALL_PADDLE_COLLISION and ball.xcor() >= RPADDLE_WALL:
        ball.xbounce()
    #
    #   rpaddle collision
    #
    if ball.distance(lpaddle) < BALL_PADDLE_COLLISION and ball.xcor() <= LPADDLE_WALL:
        ball.xbounce()
    #
    #   right paddle miss
    #
    if ball.xcor() > RIGHT_WALL:
        ball.reset()
        scoreboard.lpoint()
    #
    #   left paddle miss
    #
    if ball.xcor() < LEFT_WALL:
        ball.reset()
        scoreboard.rpoint()

print("end while")
screen.exitonclick()