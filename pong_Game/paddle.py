from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(cor)

    def go_Up(self):
        new_y = self.ycor() + 32
        self.goto(self.xcor(), new_y)
    def go_Down(self):
        new_y = self.ycor() - 32
        self.goto(self.xcor(), new_y)