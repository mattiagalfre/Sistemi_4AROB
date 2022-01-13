import turtle           #includo la libreria turtle per poterne usare le funzioni

griglia, screen = turtle.Turtle(), turtle.Screen()      #dichiaro e inizializzo lo schermo e l'oggetto turtle

for k in range(5):              #disegno le linee orizzontali della griglia
    griglia.forward(40)
    griglia.penup()
    griglia.goto(0, 10 * (k+1))
    griglia.pendown()

griglia.penup()     #sposto l'oggetto
griglia.right(90)
griglia.forward(10)
griglia.pendown()

for k in range(5):              #disegno le linee verticali della griglia
    griglia.forward(40)
    griglia.penup()
    griglia.goto(10 * (k+1), 40)
    griglia.pendown()

screen.exitonclick()