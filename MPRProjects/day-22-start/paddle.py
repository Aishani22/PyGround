from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("#ADD8E6")
        self.speed("fastest")
        self.penup()
        self.x = x
        self.y = y
        self.setposition(x, y)

    def moveUp(self):
        y_coord = self.ycor() + 20
        self.goto(self.xcor(), y_coord)

    def moveDown(self):
        y_coord = self.ycor() - 20
        self.goto(self.xcor(), y_coord)



