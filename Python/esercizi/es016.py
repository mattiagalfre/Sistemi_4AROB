"""Scrivi un programma in Python che chieda all'utente un numero intero n. 
Il programma deve creare una lista contente due diverse turtle, 
orientate in direzioni opposte. Ciascuna turtle disegna poi il poligono regolare a n lati."""

import turtle

def draw_poly(turtle, N, L):    
    for l in range(N):          
        turtle.forward(L)        
        turtle.left(360/N)

num = int(input("Inserisci il numero di lati: "))
poligono1 = turtle.Turtle()
poligono2 = turtle.Turtle()
screen = turtle.Screen()

poligono1.left(180)

poligoni = [poligono1, poligono2]

draw_poly(poligoni[0], num, 100)
draw_poly(poligoni[1], num, 100)

screen.exitonclick()
