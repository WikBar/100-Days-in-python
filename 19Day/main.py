from turtle import Turtle,Screen
from random import randint

screen=Screen()
color=screen.textinput(title="Which turtle?",prompt="Which one turtle will be first?")
all_turtles=[]
print(color)
colors=["red","blue","yellow","green","black"]




for turtle_index in range(5):
    
    tim=Turtle(shape="turtle")
    tim.speed(10)
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-350,y=-160+turtle_index*50)
    all_turtles.append(tim)

if color:
    raceOn=True
    
while raceOn:
    for turtle in all_turtles:
        
        distance=randint(2,10)
        
        turtle.forward(distance)
        
        if turtle.xcor()>230:
            print(turtle.pencolor())
            if turtle.pencolor()==color:
                print("You win the bet")
                raceOn=False
                break
            else:
                print("You lose")
                raceOn=False
                break
            



screen.exitonclick()


