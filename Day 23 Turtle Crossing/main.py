import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
nr_cars = 10


game_is_on = True
screen.listen()
#Move the turtle with keypress "Up"
screen.onkey(player.go_up, "Up")
while game_is_on:
    cars.create_car()
    time.sleep(0.1)
    screen.update()
    cars.move_car()
    #Detect collision with car
    for car in cars.all_car:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on =  False

    # Detecting when turtle reaches the finish line
    if player.is_at_finish_line():
        cars.level_up()
        scoreboard.increase_score()

screen.exitonclick()