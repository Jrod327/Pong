from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(0, -310)
        self.hideturtle()
        self.color("white")
        self.score_left = 0
        self.score_right = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 195)
        self.write(self.score_left, align=ALIGNMENT, font=FONT)
        self.goto(100, 195)
        self.write(self.score_right, align=ALIGNMENT, font=FONT)

    def increase_score_left(self):
        self.clear()
        self.score_left += 1
        self.update_scoreboard()

    def increase_score_right(self):
        self.clear()
        self.score_right += 1
        self.update_scoreboard()
