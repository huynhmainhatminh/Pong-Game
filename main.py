from turtle import Screen, Turtle
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

# Tạo đối tượng Turtle để vẽ đường sọc trắng ở giữa
center_line = Turtle()
center_line.hideturtle()
center_line.color("white")
center_line.pensize(5)
center_line.penup()
center_line.goto(0, 300)  # Bắt đầu từ đỉnh màn hình

# Vẽ đường nét đứt
def draw_dashed_line():
    center_line.clear()  # Xóa đường cũ trước khi vẽ lại
    center_line.penup()
    center_line.goto(0, 300)  # Đặt lại vị trí đầu
    for _ in range(15):  # Vẽ 15 đoạn nét đứt
        center_line.pendown()
        center_line.sety(center_line.ycor() - 20)  # Vẽ đoạn dài 20 pixel
        center_line.penup()
        center_line.sety(center_line.ycor() - 20)  # Bỏ qua 20 pixel

# Biến để theo dõi trạng thái phím
r_paddle_up = False
r_paddle_down = False
l_paddle_up = False
l_paddle_down = False

# Hàm xử lý khi nhấn phím
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

# Hàm xử lý khi thả phím
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

# Gán phím
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
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Vẽ đường nét đứt ở giữa
    draw_dashed_line()

    # Di chuyển paddle dựa trên trạng thái phím
    if r_paddle_up and r_paddle.ycor() < 250:
        r_paddle.up()
    if r_paddle_down and r_paddle.ycor() > -250:
        r_paddle.down()
    if l_paddle_up and l_paddle.ycor() < 250:
        l_paddle.up()
    if l_paddle_down and l_paddle.ycor() > -250:
        l_paddle.down()

    # Kiểm tra va chạm với trần hoặc sàn
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Kiểm tra va chạm với paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Kiểm tra khi bóng vượt qua paddle phải
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    # Kiểm tra khi bóng vượt qua paddle trái
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

screen.exitonclick()
