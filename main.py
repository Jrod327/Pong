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
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with ceiling/floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    elif ball.distance(paddle_left) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Missed ball, one of the players scores
    if ball.xcor() > 400:
        scoreboard.increase_score_left()
        ball.reset_ball()
    elif ball.xcor() < -400:
        scoreboard.increase_score_right()
        ball.reset_ball()

screen.exitonclick()
