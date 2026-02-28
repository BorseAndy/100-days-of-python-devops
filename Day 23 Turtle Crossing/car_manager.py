from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_LIMIT= (-250, 250)
X_LIMIT= (-280, 280)


class CarManager():
    def __init__(self):
        self.all_car = []
        self.start_speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            random_y = random.randint(Y_LIMIT[0], Y_LIMIT[1])
            new_car.goto(300, random_y)
            self.all_car.append(new_car)

    def move_car(self):
        for car in self.all_car:
            #Move each individual car turtle to the left
            car.backward(self.start_speed)
            #Checking if car position is out of space
            #If it's out of space it will be moved back to the right with new y coordinates
            #This method is not feasible because this leads to fload the screen after a while
            # if car.xcor() < -320:
            #     car.goto(300, random.randint(Y_LIMIT[0], Y_LIMIT[1]))

    def level_up(self):
        self.start_speed += MOVE_INCREMENT