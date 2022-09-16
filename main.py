from turtle import Turtle, Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
turtle = Turtle()
ball = Ball()
paddle_left = Paddle(x_pos=-350)
paddle_right = Paddle(x_pos=350)
scoreboard = Scoreboard()

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    elif ball.distance(paddle_left) < 50 and ball.xcor() < -340:
        ball.bounce_x()

"""
scoring logic - if ball xcor > 400 or < -400, add point to other paddle score. Reset ball to beginning
"""


screen.exitonclick()
# TODO 4 Create the ball and make it move
# TODO 5 Detect collision with wall and bounce
# TODO 6 Detect collision with a paddle
# TODO 7 Increase opposite paddle score when paddle misses

