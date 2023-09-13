from turtle import Turtle

Align = "center"
Font = ('Arial', 24, 'normal')

class scoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.goto(0,262)
        self.color("white")
        self.updateScore()

    def updateScore(self):
        self.write(arg=f"Score : {self.score}", align=Align, font=Font)

    def Score(self):
        self.score += 1
        self.clear()
        self.updateScore()

    def gameOver(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=Align, font=Font)