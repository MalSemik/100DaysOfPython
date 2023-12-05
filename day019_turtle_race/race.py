from turtle import Turtle, Screen
import random


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

pos_x = -230
pos_y = -100
turtles = []
for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(pos_x, pos_y)
    pos_y += 40
    turtles.append(t)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    chosen_turtle = random.choice(turtles)
    chosen_turtle.forward(random.randint(0,10))
    if chosen_turtle.xcor() >= 230:
        winner = chosen_turtle.color()[0]
        print(f"Winner: {winner}")
        if user_bet == winner:
            print(f"You win. The {winner} turtle won the race.")
            is_race_on = False
        else:
            print(f"You lose. The {winner} turtle won the race.")
            is_race_on = False

screen.exitonclick()
