from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.color("black")
        self.goto(STARTING_POSITION)

    def moveForward(self):
        self.forward(MOVE_DISTANCE)

    def resetPosition(self):
        self.goto(STARTING_POSITION)

