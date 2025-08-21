from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG - The Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with floor or ceiling
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect right paddle miss
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    # detect left paddle miss
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()


screen.exitonclick()