#Python pong
#By codecademy

import turtle
#import os

#Game window
window = turtle.Screen()
window.title("Pong game")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

#Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("DarkMagenta")
paddleA.shapesize(stretch_wid=6, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("DarkMagenta")
paddleB.shapesize(stretch_wid=6, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("DarkMagenta")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

#pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align = "center", font = ("Courier", 24, "normal"))

#Function to motion

#PaddleA
def paddleAUp():
  yA = paddleA.ycor()
  yA += 20
  paddleA.sety(yA)

def paddleADown():
  yA = paddleA.ycor()
  yA -= 20
  paddleA.sety(yA)

#PaddleB
def paddleBUp():
  yB = paddleB.ycor()
  yB += 20
  paddleB.sety(yB)

def paddleBDown():
  yB = paddleB.ycor()
  yB -= 20
  paddleB.sety(yB)

#Keyboard binding

#PaddleA
window.listen()
window.onkeypress(paddleAUp, "w")

window.listen()
window.onkeypress(paddleADown, "s")

#PaddleB
window.listen()
window.onkeypress(paddleBUp, "Up")

window.listen()
window.onkeypress(paddleBDown, "Down")

#Score
scoreA = 0
scoreB = 0

#Main game loop
while True:
  window.update()

  #Move the ball
  ball.setx(ball.xcor()+ball.dx)
  ball.sety(ball.ycor()+ball.dy)

  #Border checking
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1
    #os.system("aplay sound.ext&")

  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1
    #os.system("aplay sound.ext&")

  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
    scoreA += 1
    pen.clear()
    pen.write("Player A: {}    Player B: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))


  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    scoreB += 1
    pen.clear()
    pen.write("Player A: {}    Player B: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))


  #Paddle and ball collision  
  #PaddleA
  if (ball.xcor() < -330 and ball.xcor() > -350) and ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50:
    ball.setx(-330)
    ball.dx *= -1

  #paddleB
  if (ball.xcor() > 330 and ball.xcor() < 350) and ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50:
    ball.setx(330)
    ball.dx *= -1
    
