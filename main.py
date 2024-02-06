import time
import turtle
from turtle import Screen
from snake import Snake
from snakefood import Foods
from scoreboard import ScoreBoard
turtle.colormode(255)

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.tracer(0)
my_screen.screensize(600, 600)
my_screen.title("snake game 1.0")
my_screen.listen()
accountant = ScoreBoard()


snake = Snake()
food = Foods()
my_screen.update()

# def move_right():
#     snake.segments[0].setheading(0)
# def move_ups():
#     snake.segments[0].setheading(90)
# def move_left():
#     snake.segments[0].setheading(180)
# def move_down():
#     snake.segments[0].setheading(270)
#
# my_screen.onkey(key="Right", fun=move_right)
# my_screen.onkey(key="Up", fun=move_ups)
# my_screen.onkey(key="Left", fun=move_left)
# my_screen.onkey(key="Down", fun=move_down)

my_screen.onkey(key="Right", fun=snake.right)
my_screen.onkey(key="Up", fun=snake.up)
my_screen.onkey(key="Left", fun=snake.left)
my_screen.onkey(key="Down", fun=snake.down)


def detect_collision_with_self():
    global game_is_on
    for _ in snake.segments[1:]:
        if snake.segments[0].distance(_) < 1:
            accountant.reset()
            snake.reset()


def detect_collision_with_wall():
    global game_is_on
    if snake.segments[0].xcor() > 320 or snake.segments[0].xcor() < -320 \
            or snake.segments[0].ycor() < -320 or snake.segments[0].ycor() > 320:
        accountant.reset()
        snake.reset()
        game_is_on = False



game_is_on = True
while game_is_on:
    snake.move()
    my_screen.update()
    time.sleep(0.1)

    detect_collision_with_wall()
    detect_collision_with_self()

    d = snake.segments[0].distance(food)
    if d < 15:
        food.refresh()
        snake.extend()
        accountant.add_score()

# my problem: how to detect collision?: |xcor|
# how to add to the snake body? add to the last item[-1]

my_screen.exitonclick()