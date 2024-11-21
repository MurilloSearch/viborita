import random as r
import turtle as t

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.shapesize(0.5,0.5)
        self.speed('fastest')
        self.refresh()
    
    def refresh(self):        
        random_x = r.randint(-200,200)
        random_y = r.randint(-200,200)
        self.goto(random_x,random_y)

