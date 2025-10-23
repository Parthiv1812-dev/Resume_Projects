# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# list_colors = []
#
#
# for color in colors:
#     red = color.rgb[0]
#     green = color.rgb[1]
#     blue = color.rgb[2]
#     my_tuple = (red,green,blue)
#     list_colors.append(my_tuple)
#
# print(list_colors)
import turtle
from turtle import Turtle, Screen
import random

# each dot should be around 20 in size and spaced apart by 50 paces
timmy = Turtle()

timmy.speed("fastest")
turtle.colormode(255)



color_list = [(2, 9, 30), (121, 95, 41), (71, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (34, 90, 27), (150, 92, 115), (7, 154, 72), (205, 64, 92), (168, 129, 77), (1, 64, 147), (220, 178, 218), (4, 221, 218), (3, 78, 28), (79, 134, 179), (129, 157, 178), (80, 110, 137), (120, 184, 163), (120, 13, 32), (12, 214, 221), (132, 224, 210), (243, 205, 7), (229, 174, 166)]
timmy.penup()
timmy.backward(300)
timmy.left(270)
timmy.forward(300)
timmy.setheading(0)
j = 0
while j != 10:
    for i in range(10):

        timmy.color(random.choice(color_list))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    timmy.penup()
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(10*50)
    timmy.setheading(0)
    j += 1

timmy.hideturtle()
screen = Screen()
screen.exitonclick()