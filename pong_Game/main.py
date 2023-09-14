import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreBoard import scoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreBoard = scoreBoard()

screen.listen()
screen.onkey(r_paddle.go_Up, "Up")
screen.onkey(r_paddle.go_Down, "Down")
screen.onkey(l_paddle.go_Up, "w")
screen.onkey(l_paddle.go_Down, "s")







game_On = True
while game_On:
    time.sleep(ball.ball_speed)
    ball.move()
    screen.update()

    #detect with wall

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    #detect with r_paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect score

    if ball.xcor() > 380:
        scoreBoard.l_point()
        ball.ball_reset()

    if ball.xcor() < -380:
        scoreBoard.r_point()
        ball.ball_reset()

    if scoreBoard.l_score >= 5 or scoreBoard.r_score >= 5:
        game_On = False

screen.exitonclick()