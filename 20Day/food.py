from turtle import Turtle
from random import randint
from snake import Snake

class Food:
    
    def __init__(self):
        self.position = 0
        self.food = self.createFood()
        
    def createFood(self):
        x_pos=randint(0,20)
        y_pos=randint(0,20)
        food=Turtle()
        food.penup()
        food.shape("circle")
        food.color("red")
        food.goto(-200+20*x_pos,-200+20*y_pos)
    
    def removeFood(self,Snake):
        if Snake.head.xcor()==self.food.xcor() and Snake.head.ycor()==self.food.ycor():
            self.createFood()