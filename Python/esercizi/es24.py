import turtle

class Quadrato():
    def __init__ (self):
        self.lato = 0
        self.x = 0
        self.y = 0

    def setLato(self, lungLato):
        self.lato = lungLato

    def getLato(self):
        return self.lato

    def puntoStart(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def area(self):
        area = self.lato * self.lato
        return area

    def perimetro(self):
        perimetro = self.lato * 4
        return perimetro

    def isOutside(self, xPunto, yPunto):
        ok = True
        if xPunto > self.x and xPunto < (self.x + self.lato):
            if yPunto > self.y and yPunto < (self.y + self.lato):
                ok = False

        return ok

    def draw(self):
        self.quadrato = turtle.Turtle()
        self.screen = turtle.Screen()

        self.quadrato.penup()   
        self.quadrato.goto(self.x, self.y)
        self.quadrato.pendown()

        for _ in range(4):
            self.quadrato.forward(self.lato)
            self.quadrato.right(90) 

        self.screen.exitonclick()

def main():
    q = Quadrato()
    lato = int(input("Inserisci la misura del lato del quadrato: "))
    q.setLato(lato)
    x = int(input("Inserisci il valore x del vertice in alto a sinistra del quadrato: "))
    y = int(input("Inserisci il valore y del vertice in alto a sinistra del quadrato: "))
    q.puntoStart(x, y)
    print(f"L'area del quadrato vale {q.area()} cm2")
    print(f"Il perimetro del quadrato vale {q.perimetro()} cm")
    xPunto = int(input("Inserisci il valore x del punto da controllare: "))
    yPunto = int(input("Inserisci il valore y del punto da controllare: "))
    if q.isOutside(xPunto, yPunto) == True:
        print("Il punto scelto è esterno al quadrato")
    else:
        print("Il punto scelto è interno al quadrato")
    
    q.draw()

if __name__ == "__main__":
    main()