from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import scoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = scoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #distance
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBoard.Score()

    #detect wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreBoard.gameOver()
        game_on = False

    #detect tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreBoard.gameOver()
            game_on = False


screen.exitonclick()


