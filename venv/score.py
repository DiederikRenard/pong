from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_one = 0
        self.score_two = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.color("white")
        self.write(f"{self.score_one}   {self.score_two}", align="center", font=("Ariel", 50, "bold"))

    def add_score_one(self):
        self.clear()
        self.score_one += 1
        self.write(f"{self.score_one}   {self.score_two}", align="center", font=("Ariel", 50, "bold"))

    def add_score_two(self):
        self.clear()
        self.score_two += 1
        self.write(f"{self.score_one}    {self.score_two}", align="center", font=("Ariel", 50, "bold"))