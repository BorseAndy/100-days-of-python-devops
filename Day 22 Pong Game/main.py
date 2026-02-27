from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
#TODO 1: Create the screen
SCREEN_COLOR = "black"
SCREEN_TITLE = "Pong Game made by Borse Andreas-Flaviu"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
#Set the screen size
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)    # Disable screen updates for faster drawing



# #TODO 2: Create the paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))

# TODO 3: Create the ball
ball = Ball()

# TODO 4: Create Scoreboard
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with r_paddle or l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect when ball misses right paddle
    if  ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset()

    # Detect when ball misses right paddle
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset()



screen.exitonclick()