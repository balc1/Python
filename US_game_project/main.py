import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
df2 = df.state.to_list()


states = df["state"]

cor_x = df["x"]
cor_y = df["y"]

def answer_question(answer):
    answr = df[df['state'] == answer]

    # "x" ve "y" değerlerine erişelim
    x_value = answr['x'].values[0]
    y_value = answr['y'].values[0]

    turtle.penup()
    turtle.speed("fastest")
    turtle.goto(x_value, y_value)
    turtle.write(answer)
    turtle.goto(0,0)




gues_states = []
while len(gues_states) < 50:
    answer_state = screen.textinput(title=f"{len(gues_states)} / 50 States Correct",
                                    prompt="What's the another State's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in df2:
            if state not in gues_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for i in states:
        if answer_state == i:
            gues_states.append(answer_state)
            answer_question(answer_state)



