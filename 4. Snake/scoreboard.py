from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}   High score: {self.high_score}", move=False, align="center", font=("Courier", 24, "normal"))

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score}   High score: {self.high_score}", move=False, align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_update()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align="center", font=("Courier", 50, "normal"))
