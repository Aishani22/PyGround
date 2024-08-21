import random
from turtle import Turtle

COLOR_LIST = ["#FFFFFF", "#A9A9A9", "#6495ED", "#00BFFF", "#98FB98", "#FFFF00", "#FFA07A", "#FF69B4", "#EE82EE",
              "#9370DB", "#483D8B"]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.changeColor()
        self.speed("fastest")
        self.width = 20
        self.penup()
        self.x_move = 9
        self.y_move = 10
        self.move_speed = 0.1

    def changeColor(self):
        self.color(random.choice(COLOR_LIST))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.8
        self.changeColor()

    def resetGame(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
        self.changeColor()
