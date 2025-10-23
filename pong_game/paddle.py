from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(UP)
        self.penup()
        self.color("white")
        self.speed("fastest")

    def start_position(self, position):
        self.goto(position)
        self.showturtle()


    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)


