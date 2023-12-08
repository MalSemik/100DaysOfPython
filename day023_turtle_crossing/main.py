import time
from turtle import Screen
from player import Player
from grass import Grass
from car_manager import CarManager
from scoreboard import Scoreboard


def play_again():
    return True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)
grass_down = Grass((0, -280))
grass_up = Grass((0, 280))
player = Player()
cars = []
for i in range(20):
    car = CarManager()
    cars.append(car)
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 265:
        scoreboard.increase_level()
        for car in cars:
            car.speed_up()
        player.reset_position()

    for car in cars:
        car.move()
        if car.xcor() < - 310:
            car.reset_position()

        # detect collision with car:
        if player.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()
