"""
    def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if front_is_clear():
        move()
    if wall_in_front() and wall_on_right():
        turn_left()
    if right_is_clear():
        turn_right()

while not at_goal():
    jump()
"""