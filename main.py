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

# Biến để theo dõi trạng thái phím (giữ nguyên từ code trước)
r_paddle_up = False
r_paddle_down = False
l_paddle_up = False
l_paddle_down = False

# Hàm xử lý khi nhấn phím (giữ nguyên)
def r_paddle_up_press():
    global r_paddle_up
    r_paddle_up = True

def r_paddle_down_press():
    global r_paddle_down
    r_paddle_down = True

def l_paddle_up_press():
    global l_paddle_up
    l_paddle_up = True

def l_paddle_down_press():
    global l_paddle_down
    l_paddle_down = True

# Hàm xử lý khi thả phím (giữ nguyên)
def r_paddle_up_release():
    global r_paddle_up
    r_paddle_up = False

def r_paddle_down_release():
    global r_paddle_down
    r_paddle_down = False

def l_paddle_up_release():
    global l_paddle_up
    l_paddle_up = False

def l_paddle_down_release():
    global l_paddle_down
    l_paddle_down = False

# Gán phím (giữ nguyên)
screen.listen()
screen.onkeypress(r_paddle_up_press, "Up")
screen.onkeypress(r_paddle_down_press, "Down")
screen.onkeyrelease(r_paddle_up_release, "Up")
screen.onkeyrelease(r_paddle_down_release, "Down")
screen.onkeypress(l_paddle_up_press, "w")
screen.onkeypress(l_paddle_down_press, "s")
screen.onkeyrelease(l_paddle_up_release, "w")
screen.onkeyrelease(l_paddle_down_release, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Giữ cố định, không thay đổi trong game
    screen.update()
    ball.move()

    # Di chuyển paddle dựa trên trạng thái phím (giữ nguyên)
    if r_paddle_up and r_paddle.ycor() < 250:
        r_paddle.up()
    if r_paddle_down and r_paddle.ycor() > -240:
        r_paddle.down()
    if l_paddle_up and l_paddle.ycor() < 250:
        l_paddle.up()
    if l_paddle_down and l_paddle.ycor() > -240:
        l_paddle.down()

    # Kiểm tra va chạm với trần hoặc sàn (giữ nguyên)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Kiểm tra va chạm với paddle (giữ nguyên)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Kiểm tra khi bóng vượt qua paddle phải (giữ nguyên)
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    # Kiểm tra khi bóng vượt qua paddle trái (giữ nguyên)
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

screen.exitonclick()
