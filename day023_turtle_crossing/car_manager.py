from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANES = list(range(-240, 240, 30))
SPEEDS = ['fastest', 'fast', 'normal', 'slow']


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.right(180)
        self.goto(random.randint(-300, 300), random.choice(LANES))
        self.current_speed = MOVE_INCREMENT

    def move(self):
        self.forward(self.current_speed)

    def reset_position(self):
        self.goto(310, random.choice(LANES))

    def speed_up(self):
        self.current_speed += 5
