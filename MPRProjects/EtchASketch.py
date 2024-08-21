from turtle import Turtle, Screen
from tkinter import messagebox

kanos = Turtle()
screen = Screen()
screen.title("Etch A Sketch")
messagebox.showinfo("Instructions", "1. Use W and S keys to move forward and backward respectively."
                                    "\n\n2. Use A and D keys to change the angle.\n\n3. Use SPACEBAR to draw an arc.")

def moveForward():
    kanos.forward(40)


def moveBackwards():
    kanos.backward(40)


def counterClockwise():
    kanos.left(20)


def clockWise():
    kanos.right(20)


def drawCurve():
    kanos.circle(70, 90)


def undoStep():
    kanos.undo()


def clearDrawing():
    kanos.clear()
    kanos.penup()
    kanos.setposition(0, 0)
    kanos.pendown()


screen.listen()
screen.onkey(moveForward, "w")
screen.onkey(moveBackwards, "s")
screen.onkey(counterClockwise, "a")
screen.onkey(clockWise, "d")
screen.onkey(drawCurve, "space")
screen.onkey(undoStep, "u")
screen.onkey(clearDrawing, "c")
screen.exitonclick()
