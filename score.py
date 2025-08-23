from turtle import Turtle

class Score(Turtle):
    def __init__(self, left_player_name, right_player_name):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.left_player_name = left_player_name
        self.right_player_name = right_player_name
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()

    def check_winner(self):
        if self.l_score >= 10:
            self.goto(0, 0)
            self.write(f"{self.left_player_name} Wins!", align="center", font=("Courier", 40, "bold"))
            return True
        elif self.r_score >= 10:
            self.goto(0, 0)
            self.write(f"{self.right_player_name} Wins!", align="center", font=("Courier", 40, "bold"))
            return True
        return False
