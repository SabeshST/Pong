from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 78, "bold")
class ScoreKeeper(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.hideturtle()
        self.turtlesize(20,100)
        self.penup()
        # self.score_update()

    def score_update(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, the_scorer):
        self.score += 1
        self.clear()
        self.score_update()
        # self.teleport(0,100)
        # self.write(f"{the_scorer} player scored.", font=("Courier", 40, "Center"))
