from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(2, 0.3)
        self.goto(x, y)
        self.vel_y = 10

    def move(self):
        self.goto(self.xcor(), self.ycor() + self.vel_y)
