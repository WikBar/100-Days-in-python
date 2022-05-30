from turtle import Turtle

START_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.snake=[]
        self.createSnake()
        self.head=self.snake[0]
        
    def createSnake(self):
        
        for position in START_POSITION:
            new_segment=Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.snake.append(new_segment)
        
    def move(self):
        
        for item in range(len(self.snake)-1,0,-1):
            new_x=self.snake[item-1].xcor()
            new_y=self.snake[item-1].ycor()
            self.snake[item].goto(x=new_x,y=new_y)
        
        self.snake[0].forward(MOVE_DISTANCE)
    
    def Forward(self):
        if self.head.heading!=DOWN:
            self.snake[0].setheading(UP)
    def Down(self):
        if self.head.heading!=UP:
            self.snake[0].setheading(DOWN)
    def Left(self):
        if self.head.heading!=RIGHT:
            self.snake[0].setheading(LEFT)
    def Right(self):
        if self.head.heading!=LEFT:
            self.snake[0].setheading(RIGHT)
            
    
    
