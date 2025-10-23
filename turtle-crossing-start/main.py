import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
POS = (0, -280)
turtle = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(turtle.move_forward, "Up")
turtle.start_position(POS)
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
# detect  collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False
# detect successful crossing:

    if turtle.ycor() > 280:
        turtle.start_position(POS)
        car_manager.level_up()
        scoreboard.increase_level()








screen.exitonclick()