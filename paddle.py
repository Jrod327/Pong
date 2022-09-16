from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.speed(0)
        self.width = 1
        self.height = 5
        self.x_pos = x_pos
        self.y_pos = 0
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.setheading(90)
        self.penup()
        self.shapesize(stretch_wid=self.width, stretch_len=self.height)
        self.color("white")
        self.goto(self.x_pos, self.y_pos)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)

