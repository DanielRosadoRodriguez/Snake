from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

scr = Screen()
scr.bgcolor("black")
scr.tracer(0)
scr.setup(width=600, height=600)

joselito = Snake()
food = Food()
scoreboard = ScoreBoard()

scr.update()
game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.5)
    scr.listen()
    scr.onkey(key="w", fun=joselito.up)
    scr.onkey(key="s", fun=joselito.down)
    scr.onkey(key="a", fun=joselito.left)
    scr.onkey(key="d", fun=joselito.right)

    joselito.move()
    if joselito.head.distance(food) < 15:
        scoreboard.add_counter()
        scoreboard.print_counter()
        joselito.extend()
        food.refresh()

    if joselito.head.xcor() > 280 \
            or joselito.head.xcor() < -280 \
            or joselito.head.ycor() > 280 \
            or joselito.head.ycor() < -280:
        scoreboard.update_score()
        scoreboard.print_game_over()
        game_is_on = False

    for segment in joselito.segments[1:]:
        if joselito.head.distance(segment) < 10:
            scoreboard.update_score()
            scoreboard.print_game_over()
            game_is_on = False

scr.exitonclick()
