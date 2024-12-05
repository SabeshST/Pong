import turtle
from turtle import Turtle


class Player(Turtle):
    def __init__(self, up_key, down_key):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.shapesize(1,3)
        self.up_key = up_key
        self.down_key = down_key
        #input("Enter the down key for this player: ")
        # print(self.up_key, self.down_key)

        turtle.onkeypress(key=up_key, fun=self.up)
        turtle.onkeypress(key=down_key, fun=self.down)

    def up(self):
        if self.ycor() < 345:
            self.forward(20)


    def down(self):
        if self.ycor() > -335:
            self.backward(20)





