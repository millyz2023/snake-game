from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 22, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.left(90)
        self.forward(290)
        self.refresh_score()

    def add_score(self):
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"current score: {self.score}, high score: {self.high_score}", font=FONT, align=ALIGN)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.refresh_score()
