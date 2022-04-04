import Pile_Code as pc

def main():
    c1 = pc.Coda()
    
    risposta = "si"
    nElem = 0
    while(risposta == "si"):
        elemento = int(input("Inserisci il nuovo elemento della coda: "))
        c1.enqueue(elemento)
        nElem += 1
        risposta = input("Vuoi inserire altri elementi? ('si' per continuare): ")
    
    print("CODA ORIGINALE: ")
    c1.print()

    p1 = pc.Pila()

    for _ in range(nElem):
        p1.push(c1.dequeue())
    
    c2 = pc.Coda()
    for _ in range(nElem):
        c2.enqueue(p1.pop())

    print("CODA INVERTITA: ")
    c2.print()

if __name__ == "__main__":
    main()