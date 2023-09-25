from turtle import Turtle

class MiddleLine:
    def __init__(self):
        self.middle_line = Turtle()
        self.middle_line.color("white")
        self.middle_line.penup()
        self.middle_line.goto(x=0, y=400)
        self.middle_line.setheading(270)
        self.middle_line.pensize(5)
        self.middle_line.speed(0)

    def set_line(self):
        for _ in range(50):
            self.middle_line.pendown()
            self.middle_line.fd(20)
            self.middle_line.penup()
            self.middle_line.fd(20)