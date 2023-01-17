from turtle import Turtle


class Alien(Turtle):

    def __init__(self, shape, points, x_pos, y_pos):
        super().__init__()
        self.speed(0)
        self.right(90)
        self.color('white')
        self.penup()
        self.shape(shape)
        self.shapesize(1.5, 1.5)
        self.vel_x = 5
        self.points = points
        self.goto(x_pos, y_pos)

    def move(self):
        self.goto(self.xcor() - self.vel_x, self.ycor())
