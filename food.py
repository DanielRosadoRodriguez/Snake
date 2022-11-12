from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5)
        self.refresh()

    def refresh(self):
        self.goto(randint(-250, 250), randint(-250, 250))
