import turtle
from turtle import Turtle
import random
turtle.colormode(255)


class Foods:

    def __init__(self):
        self.fooddot = []

    def create_food(self):
        r_x = random.randint(-260, 260)
        r_y = random.randint(-260, 260)
        random_cor = (r_x, r_y)
        single_food = Turtle("circle")
        single_food.penup()
        single_food.goto(random_cor)
        single_food.color(self.random_color())
        self.fooddot.append(single_food)

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color_tuple = (r, g, b)
        return random_color_tuple
