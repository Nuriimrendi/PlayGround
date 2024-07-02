from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class RestartGame(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.drawButton()

    def restartGame(self):
        pass
    
    def drawButton(self):
        self.penup()
        self.goto(-77,-112)
        self.pensize(3)
        self.pendown()
        for _ in range(2):
            self.forward(150)
            self.left(90)
            self.forward(50)
            self.left(90)
        self.penup()
        self.goto(0,-100)
        self.write("Restart", False, ALIGNMENT, FONT)
    