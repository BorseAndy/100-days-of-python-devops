from turtle import Turtle

BALL_WIDTH = 20
BALL_HEIGHT = 20
BALL_XPOS = 0
BALL_YPOS = 0
BALL_SHAPE = "circle"
BALL_COLOR = "white"
MOVING_STEP = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.penup()
        self.goto(BALL_XPOS, BALL_YPOS)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(BALL_XPOS, BALL_YPOS)
        self.move_speed = 0.1
        self.x_move *= -1
