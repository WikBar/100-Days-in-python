from re import T
from turtle import Turtle, Screen
import random

timmy=Turtle()
colors={3:"red",4:"green",5:"blue",6:"pink",7:"orange",8:"black",9:"white",10:"yellow"}
directions=[0,90,180,270]
timmy.pensize(5)
timmy.speed(8)
for i in range(100):
    colorsRand=random.randint(3,10)
    directRand=random.randint(0,3)
    timmy.forward(random.randint(25,50))
    timmy.color(colors[colorsRand])
    timmy.rt(directions[directRand])

