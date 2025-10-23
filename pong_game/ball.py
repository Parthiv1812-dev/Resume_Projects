from turtle import Turtle

UP = 90
DIAGONAL = 45

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.color("white")
        self.speed("slow")
        self.x = 10
        self.y = 10
        self.value = 0.1


    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y *= -1


    def bounce_x(self):
        self.x *= -1
        #every time the ball bounces on the paddle the speed will increase
        self.value *= 0.9


    def reset_position(self):
        self.goto(0,0)
        self.value = 0.1
        self.bounce_x()

    # def bounce_down(self):
    #     new_x = self.xcor() + 10
    #     new_y = self.ycor() - 10
    #     self.goto(new_x, new_y)
    #
    # def bounce_up(self):
    #     new_x = self.xcor() - 10
    #     new_y = self.ycor() + 10
    #     self.goto(new_x, new_y)

