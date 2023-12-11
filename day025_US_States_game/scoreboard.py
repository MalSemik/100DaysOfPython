from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self, state, x, y):
        self.goto(x, y)
        self.write(state, align="center", font=("Courier", 16, "normal"))


