from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:



    def __init__(self):
        self.turtles = []
        self.x = 0
        self.length = 3
        position = (0,0)
        for i in range(self.length):
            self.increase_length(position)


        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.increase_length(position)

    def increase_length(self, position):
        self.new_turtle = Turtle("square")
        self.new_turtle.color("white")
        self.new_turtle.penup()
        self.new_turtle.goto(position)
        self.turtles.append(self.new_turtle)





    def extend(self):
        self.increase_length(self.turtles[-1].position())




    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[i - 1].xcor()
            new_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reset(self):
        for seg in self.turtles:
            seg.goto(1000,  1000)

        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]