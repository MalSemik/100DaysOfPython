import turtle
import pandas as pd
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
scoreboard = Scoreboard()

df = pd.read_csv("50_states.csv")
states = df.state.to_list()

print(list(df[df.state == "Ohio"].x)[0])


state_count = 0
guessed_states = []
while state_count < 50:
    answer_state = (screen.textinput(title=f"{state_count}/50 States Correct", prompt="Type state name: ")).title()
    if answer_state in states:
        guessed_states.append(answer_state)
        states.remove(answer_state)
        state_count += 1
        x = list(df[df.state == answer_state].x)[0]
        y = list(df[df.state == answer_state].y)[0]
        scoreboard.update_scoreboard(answer_state, x, y)

screen.exitonclick()
