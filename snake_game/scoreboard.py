from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.penup()
        self.color("white")
        self.hideturtle()

    def display(self):
        self.goto(0, 280)
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("Times New Roman", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0

        self.display()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER.", align="center", font=("Times New Roman", 15, "normal"))

    def refresh(self):
        self.clear()

