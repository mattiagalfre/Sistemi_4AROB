import turtle
import random

stella = turtle.Turtle()
cielo = turtle.Screen()

class Stella():
    def __init__(self, x, y, dim):
        self.x = x
        self.y = y
        self.dim = dim

    def creaStella(self):
        stella.speed(1000)
        stella.penup()
        stella.goto(self.x, self.y)
        stella.pendown()
        for _ in range(5):
            stella.forward(self.dim)
            stella.right(144)

def main():
    for _ in range(50):
        s = Stella(random.randint(-turtle.screensize()[0], turtle.screensize()[0]), random.randint(-turtle.screensize()[1], 
                turtle.screensize()[1]), random.randint(10, 200))
        s.creaStella()
    cielo.exitonclick()

if __name__ == "__main__":
    main()
