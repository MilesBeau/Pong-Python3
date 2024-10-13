# Simple Pong made in Python3

# Importing turtle and setting up wn 
import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

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

# Ball

# Main Game Loop
while True:
    wn.update()
    



