from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    def add_segment(self, position):
        new_s = Turtle("square")
        new_s.penup()
        new_s.color("white")
        new_s.goto(position)
        self.segments.append(new_s)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def reset(self):
        for _ in self.segments:
            _.hideturtle()
        self.segments.clear()
        self.goto(0,0)
        self.create_snake()
        self.head = self.segments[0]
        self.color("white")
        self.write("Game Over", font=("Arial", 40, "bold"), align="left")





