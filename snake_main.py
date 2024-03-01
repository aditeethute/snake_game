import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("BLACK")
screen.title("My snake game")
screen.tracer(0)
wall = Turtle("square")
wall.color("white")
wall.penup()
wall.goto(280, 0)
wall.pendown()
wall.left(90)
wall.goto(280, 280)
wall.left(90)
wall.goto(-280, 280)
wall.left(90)
wall.goto(-280, -280)
wall.left(90)
wall.goto(280, -280)
wall.left(90)
wall.goto(280, 0)
wall.hideturtle()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game = True
while game:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collision with  tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
