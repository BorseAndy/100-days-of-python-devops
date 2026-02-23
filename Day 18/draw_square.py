from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
for i in range (1,5):
    tim.forward(100)
    tim.right(90)
# Create a object
screen = Screen()
screen.exitonclick()