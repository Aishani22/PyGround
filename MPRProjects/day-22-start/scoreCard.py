from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.writeScore()

    def increaseLeft(self):
        self.clear()
        self.l_score += 1
        self.writeScore()

    def increaseRight(self):
        self.clear()
        self.r_score += 1
        self.writeScore()

    def writeScore(self):
        self.setposition(100, 240)
        self.write(f"{self.l_score}", False, "center", ("Cambria", 32, "bold"))
        self.setposition(-100, 240)
        self.write(f"{self.r_score}", False, "center", ("Cambria", 32, "bold"))

    def leftWinner(self):
        self.setposition(-160, 200)
        self.write(f"Yayyy! You win!", False, "center", ("Cambria", 22, "bold"))
        self.setposition(160, 200)
        self.write(f"Opps! You lose!", False, "center", ("Cambria", 22, "bold"))

    def rightWinner(self):
        self.setposition(-160, 200)
        self.write(f"Oops! You lose!", False, "center", ("Cambria", 22, "bold"))
        self.setposition(160, 200)
        self.write(f"Yayyy! You win!", False, "center", ("Cambria", 22, "bold"))

