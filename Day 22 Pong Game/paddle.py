from turtle import Turtle

PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.penup()
        self.color(PADDLE_COLOR)
        self.shape(PADDLE_SHAPE)
        # Paddle size should be height = 100, width = 20;
        # Standard turtle shape is height = 20 width = 20;
        # We need to stretch the height 5 times
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)

    def go_up(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() -20
        self.goto(self.xcor(), new_y)