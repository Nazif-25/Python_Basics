from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


TIME_SLEPT = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')

screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(TIME_SLEPT)

    snake.move()

    score.show_score()
    if snake.head.distance(food) < 15:
        score.clear()
        snake.extend()
        food.move()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.clear()
        score.game_over()


    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     # the above code prevents game from stopping immediately because initially the first segment is the head
    #     # so the following code will detect the collision between head and the first segment which is head also, which we don't want, hence the above
    #     # is used to bypass this issue
    #
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score.clear()
    #         score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.clear()
            score.game_over()




screen.exitonclick()