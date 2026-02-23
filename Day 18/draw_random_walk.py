import random
import turtle
from turtle import Turtle, Screen
tim = Turtle()

########### Challenge 4 - RandomWalk ########
import random
from turtle import Turtle, Screen
tim = Turtle()

colours = ["CadetBlue3", "DarkSlateGray3", "gold1", "DodgerBlue3", "PaleGreen3", "NavajoWhite2",  "SeaGreen4",
           "SkyBlue1", "dark red", "orange", "indigo", "pale violet red", "spring green"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
