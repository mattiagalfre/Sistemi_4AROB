import turtle
snow = turtle.Turtle()
finestra = turtle.Screen()

f = open(".\fileFiocco.txt", "r")
righe = f.readlines()
for riga in righe:
    comando = riga.split(":")
    print(comando)
    valore = int(comando[1][:-1])
    if comando[0] == "forward":
        snow.forward(valore)
    elif comando[0] == "backward":
        snow.backward(valore)
    elif comando[0] == "left":
        snow.left(valore)
    elif comando[0] == "right":
        snow.right(valore)
    elif comando[0] == "circle":
        snow.circle(valore)
    else:
        print("Comando non trovato")

finestra.exitonclick()
f.close()