from turtle import Turtle

FONT = ("Cambria", 16, "normal")
POSITION = (-280, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.writeScore()

    def writeScore(self):
        self.goto(POSITION)
        self.write(f"LEVEL: {self.score}", False, "center", FONT)

    def increaseScore(self):
        self.clear()
        self.score += 1
        self.writeScore()

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, "center", FONT)

