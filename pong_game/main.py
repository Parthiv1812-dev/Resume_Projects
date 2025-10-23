from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

POS1 = (350,0)
POS2 = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

#create paddle1
paddle_1 = Paddle()
paddle_1.start_position(POS1)

#create paddle2
paddle_2 = Paddle()
paddle_2.start_position(POS2)

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")

ball = Ball()

scoreboard = Scoreboard()

game_is_on = True


while game_is_on:
#To increase the ball speed we need to decrease the ball.value -> which is our sleep time
    time.sleep(ball.value)
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #     while ball.xcor() < 380:
    #         time.sleep(0.1)
    #         screen.update()
    #         ball.bounce_down()
    # if ball.ycor() < -280:
    #     while ball.xcor() > -380:
    #         time.sleep(0.1)
    #         screen.update()
    #         ball.bounce_up()
    # if ball.xcor() < -380  or ball.xcor() > 380:
    #     game_is_on = False

#Detect collision with the paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:

        ball.bounce_x()


#right paddle misses:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


#left paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()











screen.exitonclick()