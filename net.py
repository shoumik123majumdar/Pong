from turtle import Turtle

class Net:
    def __init__(self):
        self.createNet()

    def createNet(self):
        volley = Turtle()
        volley.setheading(90)
        volley.ht()
        volley.color("white")
        volley.penup()
        volley.goto(0,-300)
        volley.pendown()
        volley.pensize(5)
        for int in range (30):
            volley.forward(10)
            volley.penup()
            volley.forward(10)
            volley.pendown()