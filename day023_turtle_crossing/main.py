import time
from turtle import Screen
from player import Player
from grass import Grass
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
grass_down = Grass((0, -280))
grass_up = Grass((0, 280))
player = Player()

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.distance(grass_up) < 10:
        print("You won!")
