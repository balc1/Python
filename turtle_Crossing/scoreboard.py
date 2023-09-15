from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard:
    def __init__(self):
        self.skor = 0
        self.score = Turtle()
        self.score.penup()
        self.score.hideturtle()
        self.score_up()

    def score_up(self):
        self.score.goto(-280, 250)
        self.score.write(f"Level : {self.skor}", font=FONT)

    def score_Update(self):
        self.score.clear()
        self.skor += 1
        self.score_up()

    def game_over(self):
        self.score.goto(0, 0)
        self.score.write("GAME OVER", align="center", font=FONT)
