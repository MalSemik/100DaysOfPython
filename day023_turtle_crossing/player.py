from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.left(90)
        self.shape("turtle")
        self.color("brown")
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)

    def go_left(self):
        self.goto(self.xcor()-10, self.ycor())

    def go_right(self):
        self.goto(self.xcor()+10, self.ycor())

