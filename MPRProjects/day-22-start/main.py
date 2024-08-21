import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreCard import Scoreboard
from tkinter import messagebox

screen = Screen()
screen.title("Ping Pong Ball")
screen.setup(1000, 650)
screen.bgcolor("black")
screen.tracer(0)

user_choice = int(screen.textinput("Which one to play?", "Play game with 3 points, 5 points or 7 points?: "))
messagebox.showinfo("Instructions!", "1. The right side player can move the paddle up and down using UP and"
                                     " DOWN arrow keys.\n\n2. The left side player can move the paddle up and down using"
                                     " W and S keys.\n\n3. If you miss the ball, opponent gets a point.")

y = 350
turtle = Turtle()
turtle.setposition(0, y)
turtle.hideturtle()
turtle.pensize(3)
turtle.right(90)
while y > -300:
    turtle.pencolor("white")
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    y -= 20

paddleRight = Paddle(450, 0)
paddleLeft = Paddle(-450, 0)
screen.listen()
screen.onkeypress(paddleRight.moveUp, "Up")
screen.onkeypress(paddleRight.moveDown, "Down")
screen.onkeypress(paddleLeft.moveUp, "w")
screen.onkeypress(paddleLeft.moveDown, "s")

ball = Ball()
game_on = True

score = Scoreboard()

while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    if ball.distance(paddleRight) < 50 and ball.xcor() > 420 or ball.distance(paddleLeft) < 50 and ball.xcor() < -420:
        ball.bounce_x()

    if ball.xcor() > 480:
        ball.resetGame()
        score.increaseRight()

    if ball.xcor() < -480:
        ball.resetGame()
        score.increaseLeft()

    if score.l_score == user_choice:
        print(f"Right side player is the winner!")
        score.rightWinner()
        game_on = False
    elif score.r_score == user_choice:
        print(f"Left side player is the winner!")
        score.leftWinner()
        game_on = False

screen.exitonclick()
