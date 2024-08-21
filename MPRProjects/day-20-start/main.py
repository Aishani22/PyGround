from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
from tkinter import messagebox


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

messagebox.showinfo("Instructions", "1. Use UP, DOWN, RIGHT and LEFT arrow keys to move the snake."
                                    "\n\n2. You can't reverse the direction in which the snake is moving."
                                    "\n\n3. If snake touches the wall, game over.\n\n4. Help the snake get its food.")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.moveSnake()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increaseScore()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 295 or snake.head.ycor() < -280:
        score.resetGame()
        snake.resetSnake()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.resetGame()
            snake.resetSnake()

screen.exitonclick()

