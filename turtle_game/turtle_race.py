from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("make your bet" , prompt="Which turtle will win the race? Enter a color :")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]

turtles = []

is_race = True

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_position[turtle_index])
    turtles.append(tim)

while is_race:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            is_race = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is winner!")

        rand_dis = random.randint(0, 10)
        turtle.forward(rand_dis)

screen.exitonclick()