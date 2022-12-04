from turtle import Turtle

class Paddle(Turtle):


    def __init__(self,xCor):
        super().__init__()
        self.createPaddle()
        self.xCor = xCor
        self.setLocation()


    def createPaddle(self):
        self.color("white")
        self.shape("square")
        self.shapesize(1,4)
        self.penup()



    def setLocation(self):
        self.setpos(self.xCor, 0)
        self.setheading(90)

    def up(self):
        self.forward(40)
        #newY = self.paddle.ycor() + 20
        #self.paddle.setpos(self.paddle.xcor(),newY)

    def down(self):
        self.backward(40)
        #newY = self.paddle.ycor() - 20
        #self.paddle.setpos(self.paddle.xcor(), newY)