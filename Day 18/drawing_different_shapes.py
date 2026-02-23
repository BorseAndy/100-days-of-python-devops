import random
from turtle import Turtle, Screen
tim = Turtle()

########### Challenge 3 - Draw Shapes ########
#1 triangle, 2 square, 3 pentagon, 4 hexagon, 5 heptagon, 6 octagon, 7 nonagon and 8 decagon
colours = ["CadetBlue3", "DarkSlateGray3", "gold1", "DodgerBlue3", "PaleGreen3", "NavajoWhite2",  "SeaGreen4",
           "SkyBlue1"]

def draw_shapes(number_of_side):
    angle = 360/number_of_side
    for _ in range(number_of_side):
        tim.forward(100)
        tim.right(angle)

colorcode = 0
for i in range(3, 10+1):
    side_number = i
    tim.color(random.choice(colours))
    draw_shapes(side_number)
    colorcode += 1

# Create a object
screen = Screen()
screen.exitonclick()