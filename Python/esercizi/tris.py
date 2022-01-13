def isLibera(griglia, n):
    """funzione che controlla che la cella che si vuole occupare è libera"""
    libero = False
    if griglia[n] == " ":
        libero = True
    return libero

def disegnaGriglia(griglia):
    """funzione che disegna la griglia per il gioco tris"""
    print("\n\n " + (griglia[0]) + " | " + (griglia[1]) + " | " + (griglia[2]) + " ")
    print(f"----------- ")
    print(" " + (griglia[3]) + " | " + (griglia[4]) + " | " + (griglia[5]) + " ")
    print(f"----------- ")
    print(" " + (griglia[6]) + " | " + (griglia[7]) + " | " + (griglia[8]) + " \n\n")
    

def controlloVittoria(griglia):
    vittoria = 0
    if griglia[0]=="O" and griglia[1]=="O" and griglia[2] == "O":
        vittoria = 1
    elif griglia[0]=="X" and griglia[1]=="X" and griglia[2] == "X":
        vittoria = -1
    elif griglia[3]=="O" and griglia[4]=="O" and griglia[5] == "O":
        vittoria = 1
    elif griglia[3]=="X" and griglia[4]=="X" and griglia[5] == "X":
        vittoria = -1
    elif griglia[6]=="O" and griglia[7]=="O" and griglia[8] == "O":
        vittoria = 1
    elif griglia[6]=="X" and griglia[7]=="X" and griglia[8] == "X":
        vittoria = -1
    elif griglia[0]=="O" and griglia[3]=="O" and griglia[6] == "O":
        vittoria = 1
    elif griglia[0]=="X" and griglia[3]=="X" and griglia[6] == "X":
        vittoria = -1
    elif griglia[1]=="O" and griglia[4]=="O" and griglia[7] == "O":
        vittoria = 1
    elif griglia[1]=="X" and griglia[4]=="X" and griglia[7] == "X":
        vittoria = -1
    elif griglia[2]=="O" and griglia[5]=="O" and griglia[8] == "O":
        vittoria = 1
    elif griglia[2]=="X" and griglia[5]=="X" and griglia[8] == "X":
        vittoria = -1
    elif griglia[0]=="O" and griglia[4]=="O" and griglia[8] == "O":
        vittoria = 1
    elif griglia[0]=="X" and griglia[4]=="X" and griglia[8] == "X":
        vittoria = -1
    elif griglia[2]=="O" and griglia[4]=="O" and griglia[6] == "O":
        vittoria = 1
    elif griglia[2]=="X" and griglia[4]=="X" and griglia[6] == "X":
        vittoria = -1
    
    return vittoria

def controlloPareggio(griglia):
    libera = False
    k = 0
    while libera == False and k <= 8:
        if griglia[k] == " ":
            libera = True
        k += 1

    return libera

griglia = {0:" ", 1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" "}

partitaFinita = False
vittoria = False
while(True):
    sceltaA = int(input("O inserisce il numero della casella che vuole occupare: "))
    while isLibera(griglia, sceltaA) == False:
        sceltaA = int(input("O inserisce il numero della casella che vuole occupare: "))
    
    griglia[sceltaA] = "O"
    disegnaGriglia(griglia)

    win = controlloVittoria(griglia)
    if win == 1:
        print("Ha vinto O")
    elif win == -1:
        print("Ha vinto X")
    
    if controlloPareggio == False:
        print("Pareggio")
        
    sceltaB = int(input("X inserisce il numero della casella che vuole occupare: "))
    while isLibera(griglia, sceltaB) == False:
        sceltaB = int(input("X inserisce il numero della casella che vuole occupare: "))
    
    griglia[sceltaB] = "X"
    disegnaGriglia(griglia)

    win = controlloVittoria(griglia)
    if win == 1:
        print("Ha vinto O")
    elif win == -1:
        print("Ha vinto X")
    
    if controlloPareggio == False:
        print("Pareggio")
        

