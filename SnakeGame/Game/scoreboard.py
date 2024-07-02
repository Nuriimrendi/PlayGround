from turtle import Turtle
from restgame import RestartGame

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
HIGH_SCORE_FILE = "highscore.txt"

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.totalScore = 0  # Initialize totalScore to 0
        self.highScore = self.load_high_score()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.totalScore}   High Score: {self.highScore}", False, ALIGNMENT, FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)
        self.update_high_score()
        RestartGame()

    def increase(self):
        self.totalScore += 1
        self.update_score()

    def update_high_score(self):
        if self.totalScore > self.highScore:
            self.highScore = self.totalScore
            with open(HIGH_SCORE_FILE, 'w') as file:
                file.write(str(self.highScore))

    def load_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, 'r') as file:
                return int(file.read().strip())
        except FileNotFoundError:
            return 0
        except ValueError:
            return 0
