from turtle import Turtle

FONT = ('Arial', 13, 'bold')
ALIGNMENT = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        # self.high_score =0
        with open("data.txt", mode="r") as data:
            self.high_score= int(data.read())

        self.score = 0
        self.color('white')
        self.goto(0, 275)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")

        self.score = 0
        self.update_scoreboard()



