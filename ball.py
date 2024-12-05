from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.speed_num = 1
        self.x_move = 2
        self.y_move = -1


    def move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.teleport(0,0)
        self.x_move *= -1







