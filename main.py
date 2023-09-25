from turtle import Turtle, Screen
from middle_line import MiddleLine
from paddle import Paddle
from ball import Ball
from score import Score
import time

# TODO 1: create screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.title("Pong!")
screen.tracer(0)

middle_line = MiddleLine()
middle_line.set_line()

# TODO 2: create & move paddle
# TODO 3: Create 2nd paddle

bat = Paddle(550, 0)
bat_two = Paddle(-550, 0)

score_one = 0
score_two = 0
# TODO 4: create ball n move
ball = Ball()
score = Score()

screen.listen()
screen.onkey(bat.up, "Up")
screen.onkey(bat.down, "Down")
screen.onkey(bat_two.up, "w")
screen.onkey(bat_two.down, "s")


game_is_on = True

while game_is_on:
    ball.move()
    if ball.ycor() > 370 or ball.ycor() < -370:
        ball.bounce()

    if ball.xcor() < -550 and ball.distance(bat_two) < 60:
        ball.paddle_bounce()

    if ball.xcor() > 550 and ball.distance(bat) < 60:
        ball.paddle_bounce()

    if ball.xcor() > 580:
        score.add_score_one()
        ball.ball_reset()

    if ball.xcor() < -580:
        score.add_score_two()
        ball.ball_reset()

    if score.score_one >= 11 and score.score_one > score.score_two + 2:
        game_is_on = False
        winner = "Player One"
        game_winner = Turtle()
        game_winner.color("white")
        game_winner.hideturtle()
        game_winner.write(f"{winner} is the winner!!")

    if score.score_two >= 11 and score.score_two > score.score_one + 2:
        game_is_on = False
        winner = "Player Two"
        game_winner = Turtle()
        game_winner.hideturtle()
        game_winner.color("white")
        game_winner.write(f"{winner} is the winner!!", align="center", font=("Ariel", 50, "bold"))
    screen.update()
    time.sleep(0.01)



screen.exitonclick()