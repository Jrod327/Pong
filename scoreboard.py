from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(0, -310)
        self.pencolor("white")
        self.setheading(90)
        self.pensize(5)
        for i in range(30):
            self.pendown()
            self.forward(5)
            self.penup()
            self.forward(25)
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

    def increase_score(self, paddle_side):
        self.clear()
        paddle_side += 1
        self.update_scoreboard()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -60)
        self.write(f"Press 'R' to restart or 'Q' to quit.", align=ALIGNMENT, font=("Courier", 12, "normal"))