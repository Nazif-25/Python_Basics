from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
is_race_on = False
finish_line_reached = False
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
all_turtles = []


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
count = -100

for i in colors:
    new_turtle = Turtle('turtle')
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x=-200, y= count)
    all_turtles.append(new_turtle)
    count+=30

if user_bet:
    is_race_on = True



while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The winner is {winning_color}")
            else:
                print(f"You've lost! The winner is {winning_color}")


            finish_line_reached = True
        if finish_line_reached:
            is_race_on = False

        turtle.penup()
        turtle.forward(random.randint(0,10))

# while is_race_on:
#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if user_bet == winning_color:
#                 print(f"You've won! The winner is {winning_color}")
#             else:
#                 print(f"You've lost! The winner is {winning_color}")
#
#
#         turtle.penup()
#         turtle.forward(random.randint(0, 10))



screen.exitonclick()
