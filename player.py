from turtle import Turtle


class Player(Turtle):

    def __init__(self, shape):
        super().__init__()
        self.left(90)
        self.color("white")
        self.speed(0)
        self.shape(shape)
        self.shapesize(4.5, 4.5)
        self.penup()
        self.goto(0, -240)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
        if self.xcor() <= -380:
            self.goto(-380, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
        if self.xcor() >= 380:
            self.goto(380, self.ycor())
