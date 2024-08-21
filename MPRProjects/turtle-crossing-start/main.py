import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scores import Scoreboard
from tkinter import messagebox

screen = Screen()
screen.setup(width=700, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
car_list = []

turtle = Player()
score = Scoreboard()

for _ in range(40):
    car = CarManager()
    car_list.append(car)


screen.listen()
screen.onkeypress(turtle.moveForward, "Up")

messagebox.showinfo("Instructions", "1. The turtle moves only in forward direction using UP arrow key."
                                    "\n\n2. If it crashes withs any car, game over.\n\n3. Help the turtle cross the road safely.")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for eachCar in car_list:
        if turtle.distance(eachCar) < 20:
            game_is_on = False
            score.gameOver()
        elif eachCar.xcor() < -350:
            eachCar.resetPosition()
        else:
            eachCar.moveCar()

    if turtle.ycor() > 280:
        turtle.resetPosition()
        score.increaseScore()
        for cars in car_list:
            cars.increaseSpeed()

screen.exitonclick()