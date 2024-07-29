from turtle import Turtle
COLOR = 'white'
X_POS = 0
Y_POS = 270
ALIGNMENT = 'center'
FONT = ("Arial", 20, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.show_score()


    def increase_score(self):
        self.score += 1

    def show_score(self):
        self.goto(x=X_POS, y=Y_POS)
        self.write(f"Score: {self.score}", align=ALIGNMENT,  font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER!\n Final Score: {self.score}", align=ALIGNMENT,  font=FONT)

