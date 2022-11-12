from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        for position in self.starting_positions:
            self.add_segment(position)
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            n_x = self.segments[seg_num - 1].xcor()
            n_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(n_x, n_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.segments[0].setheading(0)

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.add_segment((0, 0))
