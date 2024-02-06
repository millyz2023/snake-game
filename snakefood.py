from turtle import Turtle
import random
SHAPE = "circle"

class Foods(Turtle):

    def __init__(self):
        super().__init__()
        self.clear()
        self.list = []
        self.shape(SHAPE)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color(self.random_color())
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(self.random_color())
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color_tuple = (r, g, b)
        return random_color_tuple
