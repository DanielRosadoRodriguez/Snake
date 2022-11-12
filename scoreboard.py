from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = 0
        with open("scores.txt", mode="r") as scores_file:
            self.high_score = int(scores_file.read())
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.print_counter()
        self.hideturtle()

    def add_counter(self):
        self.counter += 1

    def print_counter(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Counter: {self.counter} HIgh Score: {self.high_score}", True, align="center")

    def print_game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", True, align="center")

    def update_score(self):
        if self.counter > self.high_score:
            self.high_score = self.counter
            with open("scores.txt", mode="w") as scores_file:
                scores_file.write(f"{self.high_score}")
        self.counter = 0
        self.print_counter()
