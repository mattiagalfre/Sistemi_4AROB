"""Scrivere un programma in Python nel quale utilizzando il modulo turtle: 
- sia presente una funzione che disegni una stella nelle coordinate x e y (passate come parametri alla funzione) 
- disegni 50 stelle sullo screen posizionate in posizioni casuali."""

import random
import turtle

stella = turtle.Turtle()
cielo = turtle.Screen()

def creaStella(x, y, punte, dim):
    stella.speed(1000)
    stella.penup()
    stella.goto(x,y)
    stella.pendown()
    for _ in range(punte):
        stella.forward(dim)
        stella.right(((360 / punte) * 2) % 180)
        
for _ in range(50):
    creaStella(random.randint(-turtle.screensize()[0],turtle.screensize()[0]),random.randint(-turtle.screensize()[1],turtle.screensize()[1]),5, random.randint(10,150))

cielo.exitonclick()