import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.go, "Up")
cars = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.car_create()
    cars.car_fors()


    #detect crash with cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #detect succesful
    if player.succes():
        player.start()
        scoreboard.score_Update()
        cars.car_Speed()

screen.exitonclick()