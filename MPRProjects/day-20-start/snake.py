from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COORDINATES_LIST = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for index in COORDINATES_LIST:
            self.addSegment(index)

    def addSegment(self, index):
        kanos = Turtle("square")
        kanos.color("white")
        kanos.speed("slowest")
        kanos.penup()
        kanos.setposition(index)
        self.segments.append(kanos)

    def resetSnake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]

    def extend(self):
        self.addSegment(self.segments[-1].position())

    def moveSnake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cor, y_cor)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
