# Simple Pong made in Python3

# Importing turtle and setting up wn 
import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_one = 0
score_two = 0

# Game Objects

# Paddle 1
paddle_one = turtle.Turtle()
paddle_one.speed(0)
paddle_one.shape("square")
paddle_one.color("white")
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
paddle_one.penup()
paddle_one.goto(-350, 0)

# Paddle 2
paddle_two = turtle.Turtle()
paddle_two.speed(0)
paddle_two.shape("square")
paddle_two.color("white")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.penup()
paddle_two.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.20
ball.dy = 0.20

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() 
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 22, "normal"))

# Functions
def paddle_one_up():
    y = paddle_one.ycor()
    y += 20
    paddle_one.sety(y)
    
def paddle_one_down():
    y = paddle_one.ycor()
    y -= 20
    paddle_one.sety(y)
    
def paddle_two_up():
    y = paddle_two.ycor()
    y += 20
    paddle_two.sety(y)
    
def paddle_two_down():
    y = paddle_two.ycor()
    y -= 20
    paddle_two.sety(y)
    
# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_one_up, "w")
wn.onkeypress(paddle_one_down, "s")
wn.onkeypress(paddle_two_up, "Up")
wn.onkeypress(paddle_two_down, "Down")



# Main Game Loop
while True:
    wn.update()
    
    # Move The Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_one += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_one, score_two), align="center", font=("Courier", 22, "normal"))
       
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_two += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_one, score_two), align="center", font=("Courier", 22, "normal"))

    # Paddle and Ball collisions 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_two.ycor() + 40 and ball.ycor() > paddle_two.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_one.ycor() + 40 and ball.ycor() > paddle_one.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
    
    