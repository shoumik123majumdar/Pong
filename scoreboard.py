from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()



    def addScore(self):
        self.score +=1
        self.clear()
        self.write(f"{self.score}", False, "center", ("Arial", 50, "bold"))

    def setPos(self,xCor,yCor):
        self.goto(xCor,yCor)
        self.write(f"{self.score}", False, "center", ("Arial", 50, "bold"))
