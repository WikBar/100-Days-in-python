import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)



snake=Snake()
food=Food()
screen.listen()
screen.onkey(snake.Forward,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")

gameOn=True

while gameOn:
    screen.update()
    time.sleep(0.2)
    
    snake.move()
    



screen.exitonclick()