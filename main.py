from turtle import Turtle, Screen
from player import Player
from scoreboard import ScoreKeeper
from ball import Ball
import time


#SCREEN SETUP
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=1200, height=800)
my_screen.title("Pong")
my_screen.listen()
my_screen.tracer(0)


#PONG NET SETUP
net_line = Turtle()
net_line.hideturtle()
net_line.teleport(0,395)
net_line.pencolor("white")
net_line.setheading(270)
while net_line.ycor() > -400:
    net_line.forward(20)
    net_line.penup()
    net_line.forward(20)
    net_line.pendown()

#BALL INITIALIZATION
ball = Ball()

#PLAYER INITIALIZATION
player_left = Player("w","s")

player_right = Player("Up","Down")

def starting_positions():
    player_left.teleport(-585, 0)
    player_right.teleport(576, 0)
    ball.reset_ball()

#SCOREKEEPR INITIALIZATION
score_keeper_left = ScoreKeeper()
score_keeper_left.goto(-50,310)
score_keeper_left.score_update()

score_keeper_right = ScoreKeeper()
score_keeper_right.goto(50,310)
score_keeper_right.score_update()


game_on = True
starting_positions()


while game_on:
    time.sleep(0.00001)
    my_screen.update()
    ball.move()

    #for when the ball hits the left or right wall
    if ((ball.xcor() > 590 or ball.xcor() < -590)):

        game_on = False

        #update score
        if ball.xcor() > 590:
            score_keeper_left.increase_score("Left")
        elif ball.xcor() < -590:
            score_keeper_right.increase_score("Right")

        time.sleep(1.5)
        starting_positions()
        game_on = True


        #screen reset the screen to game start and update the scores

    if ball.distance(player_right) < 20 and ball.xcor() > 530:
        ball.bounce_x()
        print("I happened")
    elif ball.distance(player_left) < 20 and ball.xcor() < -525:
        ball.bounce_x()
        print("other")

    if (ball.ycor() > 390 or ball.ycor() < -390):
        ball.bounce_y()


my_screen.exitonclick()