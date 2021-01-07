from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Create the screen with a width and height of 600
# Background color will be black and title set to My Snake Game
# Tracer must also be set to 0 for no animation
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create snake and food
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game will run until the snake has died
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food.xcor(), food.ycor()) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_update()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
