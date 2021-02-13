from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 80, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0

        self.hideturtle()
        self.color("white")
        self.penup()
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.lscore, align=ALIGN, font=FONT)
        self.goto(0, 190)
        self.write("-", align=ALIGN, font=FONT)
        self.goto(100, 190)
        self.write(self.rscore, align=ALIGN, font=FONT)

    def lpoint(self):
        self.lscore += 1
        self.update()

    def rpoint(self):
        self.rscore += 1
        self.update()

    def gameover(self):
        self.goto(0, -50)
        self.write("GAME OVER", align=ALIGN, font=FONT)


