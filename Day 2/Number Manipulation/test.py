logoReeborg
's World

Hurdle
4
World
Info
Python
Reeborg
's keyboard Additional options
English

reverse
step
run
step
pause
stop
reload
1 / 2
Python
CodelibraryA↑AA↓A


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right() == True:
        move()
        move += 1
    turn_right()
    move()
    turn_right()
    for i range(0, move):
        move()
    turn_left()

​
move = 0
​
while at_goal() == False:
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        jump()
