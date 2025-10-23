from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True



while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.display()
    #Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.score += 1
        snake.length += 1
        snake.extend()
        scoreboard.refresh()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    #detect collision with itself
    #My approach
    # for i in range(4, len(snake.turtles)):
    #     if snake.turtles[i].distance(snake.head) < 20:
    #         scoreboard.game_over()
    #         game_on = False
    for segment in snake.turtles[1:]:
        if segment.distance(snake.head) < 10:
            scoreboard.reset()
            snake.reset()






screen.exitonclick()