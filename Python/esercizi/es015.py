"""Scrivi un programma in Python che chieda all'utente un numero intero n 
e disegni, tramite turtle, il poligono regolare a n lati."""

import turtle

def draw_poly(turtle, N, L):    
    for l in range(N):          
        turtle.forward(L)        
        turtle.left(360/N)

lati = int(input("Inserisci il numero di lati del poligono: "))

poligono = turtle.Turtle()
screen = turtle.Screen()

draw_poly(poligono, lati, 50)

screen.exitonclick()
