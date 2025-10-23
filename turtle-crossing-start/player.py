from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.speed("fastest")

    def start_position(self, position):
        self.goto(position)
        self.showturtle()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)


    def reset_position(self):
        self.goto(0, -280)



