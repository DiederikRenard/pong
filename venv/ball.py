from turtle import Turtle
from random import randint, choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.penup()
        self.head = choice([randint(135, 225), randint(-45, 45)])
        self.setheading(self.head)
        self.speed_ball = 5


    def move(self):
        self.fd(self.speed_ball)

    def bounce(self):
        self.setheading(self.heading() * -1)


    def paddle_bounce(self):
        self.setheading(180 - self.heading())
        if self.speed_ball <= 25:
            self.speed_ball += 2
        else:
            self.speed_ball = 25


    def ball_reset(self):
        self.goto(0, 0)
        self.head = choice([randint(135, 225), randint(-45, 45)])
        self.setheading(self.head)
        self.speed_ball = 5
