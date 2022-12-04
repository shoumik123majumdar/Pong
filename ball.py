from turtle import Turtle


class Ball():
    def __init__(self):
        self.ball = Turtle()
        self.createBall()
        self.xballSpeed = 2
        self.yballSpeed = 2


    def createBall(self):
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.setpos(0,0)

    def move(self):
        newX = self.ball.xcor() + self.xballSpeed
        newY = self.ball.ycor() + self.yballSpeed
        self.ball.goto(newX,newY)


    def bounce1(self):
        self.yballSpeed = - self.yballSpeed
        self.yballSpeed *=1.1


    def bounce2(self):
        self.xballSpeed = - self.xballSpeed
        self.xballSpeed *=1.1

    def reset(self):
        self.ball.setpos(0,0)
        self.bounce2()
        self.xballSpeed = 2
        self.yballSpeed = 2

