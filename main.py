from turtle import Screen
from net import Net
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

net = Net()
screen.listen()

paddle1 = Paddle(350)
screen.onkey(paddle1.up,"Up")
screen.onkey(paddle1.down,"Down")

paddle2 = Paddle(-350)
screen.onkey(paddle2.up,"w")
screen.onkey(paddle2.down,"s")

ball = Ball()


score1 = ScoreBoard()
score1.setPos(30,240)

score2 = ScoreBoard()
score2.setPos(-30,240)

gameIsOn = True
while gameIsOn:
    screen.update()
    ball.move()
    if paddle1.ycor()>290:
        paddle1.down()
    elif paddle1.ycor()<-290:
        paddle1.up()
    elif paddle2.ycor()>290:
        paddle2.down()
    elif paddle2.ycor()<-290:
        paddle2.up()

    if (ball.ball.xcor()>=350 and ball.ball.distance(paddle1)<50) or (ball.ball.xcor()<-350 and ball.ball.distance(paddle2)<50):
        ball.bounce2()
    if ball.ball.ycor() > 280 or ball.ball.ycor() < -280:
        ball.bounce1()
    if ball.ball.xcor()>400:
        score2.addScore()
        ball.reset()


    elif ball.ball.xcor()<-400:
        score1.addScore()
        ball.reset()


screen.exitonclick()
