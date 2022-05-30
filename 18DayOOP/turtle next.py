
import turtle as t
import random

t.colormode(255)

timmy=t.Turtle()

directions=[0,90,180,270]

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)


def spirograph(num_of_circles):
    for i in range(num_of_circles):
        timmy.left(360/num_of_circles)
        timmy.circle(50)
        timmy.color(random_color())
timmy.pensize(3)
timmy.speed(10)


spirograph(10)