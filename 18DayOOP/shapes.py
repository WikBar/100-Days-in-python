from re import T
from turtle import Turtle, Screen
timmy=Turtle()
colors={3:"red",4:"green",5:"blue",6:"pink",7:"orange",8:"black",9:"white",10:"yellow"}

def draw(num_shapes):
    angle=360/num_shapes
    for _ in range(n):
        timmy.forward(100)
        timmy.rt(angle)
    
for n in range(3,10):
    timmy.color(colors[n])
    draw(n)
    


