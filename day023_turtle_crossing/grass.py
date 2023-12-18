from turtle import Turtle


class Grass(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("green")
        self.shape("square")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=2, stretch_len=100)