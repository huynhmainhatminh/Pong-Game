from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 5  # Tốc độ ban đầu chậm hơn để dễ chơi (có thể chỉnh thành 10 nếu muốn nhanh hơn)
        self.y_move = 5
        self.move_speed = 0.05  # Giữ cố định, không thay đổi để tránh lag
        self.speed_increment = 0.5  # Lượng tăng dần mỗi va chạm paddle (có thể chỉnh nhỏ hơn để tăng chậm hơn)
        self.max_speed = 15  # Giới hạn tốc độ tối đa để game không quá khó

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        # Không tăng tốc khi va tường, chỉ đảo hướng

    def bounce_x(self):
        current_speed = abs(self.x_move)
        if current_speed < self.max_speed:
            new_speed = current_speed + self.speed_increment
        else:
            new_speed = self.max_speed
        self.x_move = -new_speed if self.x_move > 0 else new_speed  # Đảo hướng và tăng tốc
        # Tăng y_move tương tự để cân bằng (nếu muốn, có thể bỏ nếu chỉ tăng theo x)
        current_y_speed = abs(self.y_move)
        if current_y_speed < self.max_speed:
            self.y_move = - (current_y_speed + self.speed_increment) if self.y_move < 0 else (current_y_speed + self.speed_increment)

    def reset(self):
        self.goto(0, 0)
        self.x_move = 5 if self.x_move > 0 else -5  # Reset về tốc độ ban đầu, giữ hướng ngẫu nhiên
        self.y_move = 5 if self.y_move > 0 else -5
        self.bounce_x()  # Đảo hướng x để bắt đầu lại
