from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(position_x, position_y)

    def up(self):
        self.setheading(90)
        self.fd(50)

    def down(self):
        self.setheading(270)
        self.fd(50)

