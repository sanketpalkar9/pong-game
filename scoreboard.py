from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.goto(0, 200)
        self.write(":", align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score+=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score+=1
        self.update_scoreboard()

    def game_over(self):

        if self.l_score > self.r_score:
            self.goto(-60, 0)
            self.write(self.l_score, align="center", font=("Courier", 30, "normal"))
            self.goto(60, 0)
            self.write(self.r_score, align="center", font=("Courier", 30, "normal"))
            self.goto(0,50)
            self.write("Game Over: Left Won", align="center", font=("Courier", 30, "normal"))

        else:
            self.goto(-60, 0)
            self.write(self.l_score, align="center", font=("Courier", 30, "normal"))
            self.goto(60, 0)
            self.write(self.r_score, align="center", font=("Courier", 30, "normal"))
            self.goto(0, 50)
            self.write("Game Over: Right Won", align="center", font=("Courier", 30, "normal"))