from turtle import Turtle


FILE = "highscore.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.highscore = self.read_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}   High score: {self.highscore}", move=False, align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Courier", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def read_highscore(self):
        with open(FILE, 'r') as file:
            self.highscore = file.read()
        return int(self.highscore)

    def update_highscore(self):
        self.highscore = self.score
        self.clear()
        self.update_scoreboard()

    def save_highscore(self, score):
        with open(FILE, 'w') as file:
            file.write(str(self.highscore))
