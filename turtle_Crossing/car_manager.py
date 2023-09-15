import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_create(self):
        chance = random.randint(1,6)
        if chance == 6:
            cars_y = random.randint(-250, 250)
            car = Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.penup()
            car.setheading(180)
            car.goto(300, cars_y)
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(car)

    def car_fors(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def car_Speed(self):
        self.car_speed += MOVE_INCREMENT