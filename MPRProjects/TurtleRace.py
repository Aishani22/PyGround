from tkinter import messagebox
import random
from turtle import Turtle, Screen

FONT = ("Cambria", 16, "normal")
POSITION = (-280, 260)

screen = Screen()
screen.setup(500, 400)
screen.title("Turtle Race")
is_race_on = False
messagebox.showinfo("Instructions", "Choose a turtle of one of the following colors to win the race:"
                                    " VIOLET, INDIGO, BLUE, GREEN, YELLOW, ORANGE, RED.")
user_bet = screen.textinput(title="Make your bet!",
                            prompt="Which turtle will win the race? Enter the color: ").lower()
colors = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]

turtle_list = []
if user_bet:
    is_race_on = True

kanos = Turtle()
kanos.shape("turtle")
kanos.color(colors[0])
kanos.penup()
kanos.goto((-230, 90))
turtle_list.append(kanos)

timmy = Turtle()
timmy.shape("turtle")
timmy.color(colors[1])
timmy.penup()
timmy.goto((-230, 60))
turtle_list.append(timmy)

daz = Turtle()
daz.shape("turtle")
daz.color(colors[2])
daz.penup()
daz.goto((-230, 30))
turtle_list.append(daz)

glenn = Turtle()
glenn.shape("turtle")
glenn.color(colors[3])
glenn.penup()
glenn.goto((-230, 0))
turtle_list.append(glenn)

mitch = Turtle()
mitch.shape("turtle")
mitch.color(colors[4])
mitch.penup()
mitch.goto((-230, -30))
turtle_list.append(mitch)

finny = Turtle()
finny.shape("turtle")
finny.color(colors[5])
finny.penup()
finny.goto((-230, -60))
turtle_list.append(finny)

rach = Turtle()
rach.shape("turtle")
rach.color(colors[6])
rach.penup()
rach.goto((-230, -90))
turtle_list.append(rach)

writeText = Turtle()
writeText.hideturtle()

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 210:
            win_color = turtle.pencolor()
            if win_color == user_bet:
                writeText.goto(0, 0)
                writeText.write(f"Yayyy! Your {win_color} turtle wins the race!", False, "center", FONT)
            else:
                writeText.goto(0, 0)
                writeText.write(f"Opps! You lose. {win_color} turtle wins the race!", False, "center", FONT)
            is_race_on = False
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()


