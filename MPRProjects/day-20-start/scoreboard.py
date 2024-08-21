from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        with open("day-20-start/data.txt") as data:
            self.highScore = int(data.read())
        self.setposition(0, 270)
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"SCORE: {self.score}         HIGH SCORE: {self.highScore}", False, "center",
                   ("Cambria", 14, "normal"))

    def increaseScore(self):
        self.score += 1
        self.updateScore()

    def resetGame(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highScore}")
        self.score = 0
        self.updateScore()


