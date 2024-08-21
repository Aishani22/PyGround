import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.positionCar()
        self.carSpeed = STARTING_MOVE_DISTANCE
        self.moveFaster = MOVE_INCREMENT
        self.positionCar()

    def positionCar(self):
        random_x = random.randint(-400, 400)
        random_y = random.randint(-240, 240)
        self.goto(random_x, random_y)

    def resetPosition(self):
        random_y = random.randint(-240, 240)
        self.goto(350, random_y)

    def moveCar(self):
        self.backward(self.carSpeed)

    def increaseSpeed(self):
        self.carSpeed += MOVE_INCREMENT


