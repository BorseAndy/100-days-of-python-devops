from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

#screen is now listening
screen.listen()
#When space it's triggered the function move forward is applied
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()