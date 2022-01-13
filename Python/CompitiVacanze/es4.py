"""Implementare il gioco Forza 4 in Python utilizzando soltanto il
terminale (https://it.wikipedia.org/wiki/Forza_quattro)"""

import sys

def controlloVittoria(griglia):
    vittoria = False
    #prima riga
    if griglia[0]==griglia[1]==griglia[2]==griglia[3] and griglia[0]!=" ":
        vittoria = True
    elif griglia[1]==griglia[2]==griglia[3]==griglia[4] and griglia[1]!=" ":
        vittoria = True
    elif griglia[2]==griglia[3]==griglia[4]==griglia[5] and griglia[2]!=" ":
        vittoria = True
    elif griglia[3]==griglia[4]==griglia[5]==griglia[6] and griglia[3]!=" ":
        vittoria = True
    #seconda riga
    elif griglia[7]==griglia[7]==griglia[9]==griglia[10] and griglia[7]!=" ":
        vittoria = True
    elif griglia[8]==griglia[9]==griglia[10]==griglia[11] and griglia[8]!=" ":
        vittoria = True
    elif griglia[9]==griglia[10]==griglia[11]==griglia[12] and griglia[9]!=" ":
        vittoria = True
    elif griglia[10]==griglia[11]==griglia[12]==griglia[13] and griglia[10]!=" ":
        vittoria = True
    #terza riga
    elif griglia[14]==griglia[15]==griglia[16]==griglia[17] and griglia[14]!=" ":
        vittoria = True
    elif griglia[15]==griglia[16]==griglia[17]==griglia[18] and griglia[15]!=" ":
        vittoria = True
    elif griglia[16]==griglia[17]==griglia[18]==griglia[19] and griglia[16]!=" ":
        vittoria = True
    elif griglia[17]==griglia[18]==griglia[19]==griglia[20] and griglia[17]!=" ":
        vittoria = True
    #quarta riga
    elif griglia[21]==griglia[22]==griglia[23]==griglia[24] and griglia[21]!=" ":
        vittoria = True
    elif griglia[22]==griglia[23]==griglia[24]==griglia[25] and griglia[22]!=" ":
        vittoria = True
    elif griglia[23]==griglia[24]==griglia[25]==griglia[26] and griglia[23]!=" ":
        vittoria = True
    elif griglia[24]==griglia[25]==griglia[26]==griglia[27] and griglia[24]!=" ":
        vittoria = True
    #quinta riga
    elif griglia[28]==griglia[29]==griglia[30]==griglia[31] and griglia[28]!=" ":
        vittoria = True
    elif griglia[29]==griglia[30]==griglia[31]==griglia[32] and griglia[29]!=" ":
        vittoria = True
    elif griglia[30]==griglia[31]==griglia[32]==griglia[33] and griglia[30]!=" ":
        vittoria = True
    elif griglia[31]==griglia[32]==griglia[33]==griglia[34] and griglia[31]!=" ":
        vittoria = True
    #sesta riga
    elif griglia[35]==griglia[36]==griglia[37]==griglia[38] and griglia[35]!=" ":
        vittoria = True
    elif griglia[36]==griglia[37]==griglia[38]==griglia[39] and griglia[36]!=" ":
        vittoria = True
    elif griglia[37]==griglia[38]==griglia[39]==griglia[40] and griglia[37]!=" ":
        vittoria = True
    elif griglia[38]==griglia[39]==griglia[40]==griglia[41] and griglia[38]!=" ":
        vittoria = True
    #prima colonna
    elif griglia[0]==griglia[7]==griglia[14]==griglia[21] and griglia[0]!=" ":
        vittoria = True
    elif griglia[7]==griglia[14]==griglia[21]==griglia[28] and griglia[7]!=" ":
        vittoria = True
    elif griglia[14]==griglia[21]==griglia[28]==griglia[35] and griglia[14]!=" ":
        vittoria = True
    #seconda colonna
    elif griglia[1]==griglia[8]==griglia[15]==griglia[22] and griglia[1]!=" ":
        vittoria = True
    elif griglia[8]==griglia[15]==griglia[22]==griglia[29] and griglia[8]!=" ":
        vittoria = True
    elif griglia[15]==griglia[22]==griglia[29]==griglia[36] and griglia[15]!=" ":
        vittoria = True
    #terza colonna
    elif griglia[2]==griglia[9]==griglia[16]==griglia[23] and griglia[2]!=" ":
        vittoria = True
    elif griglia[9]==griglia[16]==griglia[23]==griglia[30] and griglia[9]!=" ":
        vittoria = True
    elif griglia[16]==griglia[23]==griglia[30]==griglia[37] and griglia[16]!=" ":
        vittoria = True
    #quarta colonna
    elif griglia[3]==griglia[10]==griglia[17]==griglia[24] and griglia[3]!=" ":
        vittoria = True
    elif griglia[10]==griglia[17]==griglia[24]==griglia[31] and griglia[10]!=" ":
        vittoria = True
    elif griglia[17]==griglia[24]==griglia[31]==griglia[38] and griglia[17]!=" ":
        vittoria = True
    #quinta colonna
    elif griglia[4]==griglia[11]==griglia[18]==griglia[25] and griglia[4]!=" ":
        vittoria = True
    elif griglia[11]==griglia[18]==griglia[25]==griglia[32] and griglia[11]!=" ":
        vittoria = True
    elif griglia[18]==griglia[25]==griglia[32]==griglia[39] and griglia[18]!=" ":
        vittoria = True
    #sesta colonna
    elif griglia[5]==griglia[12]==griglia[19]==griglia[26] and griglia[5]!=" ":
        vittoria = True
    elif griglia[12]==griglia[19]==griglia[26]==griglia[33] and griglia[12]!=" ":
        vittoria = True
    elif griglia[19]==griglia[26]==griglia[33]==griglia[40] and griglia[19]!=" ":
        vittoria = True
    #settima colonna
    elif griglia[6]==griglia[13]==griglia[20]==griglia[27] and griglia[6]!=" ":
        vittoria = True
    elif griglia[13]==griglia[20]==griglia[27]==griglia[34] and griglia[13]!=" ":
        vittoria = True
    elif griglia[20]==griglia[27]==griglia[34]==griglia[41] and griglia[20]!=" ":
        vittoria = True
    #diagonali /
    elif griglia[21]==griglia[15]==griglia[9]==griglia[3] and griglia[21]!=" ":
        vittoria = True
    elif griglia[28]==griglia[22]==griglia[16]==griglia[10] and griglia[28]!=" ":
        vittoria = True
    elif griglia[35]==griglia[29]==griglia[23]==griglia[17] and griglia[35]!=" ":
        vittoria = True
    elif griglia[36]==griglia[30]==griglia[24]==griglia[18] and griglia[36]!=" ":
        vittoria = True
    elif griglia[37]==griglia[31]==griglia[25]==griglia[19] and griglia[37]!=" ":
        vittoria = True
    elif griglia[38]==griglia[32]==griglia[26]==griglia[20] and griglia[35]!=" ":
        vittoria = True
    elif griglia[22]==griglia[16]==griglia[10]==griglia[4] and griglia[22]!=" ":
        vittoria = True
    elif griglia[29]==griglia[23]==griglia[17]==griglia[11] and griglia[29]!=" ":
        vittoria = True
    elif griglia[30]==griglia[24]==griglia[18]==griglia[12] and griglia[30]!=" ":
        vittoria = True
    elif griglia[31]==griglia[25]==griglia[19]==griglia[13] and griglia[31]!=" ":
        vittoria = True
    elif griglia[24]==griglia[18]==griglia[12]==griglia[6] and griglia[24]!=" ":
        vittoria = True
    elif griglia[23]==griglia[17]==griglia[11]==griglia[5] and griglia[23]!=" ":
        vittoria = True
    #diagonali \
    elif griglia[3]==griglia[11]==griglia[19]==griglia[27] and griglia[3]!=" ":
        vittoria = True
    elif griglia[10]==griglia[18]==griglia[26]==griglia[34] and griglia[10]!=" ":
        vittoria = True
    elif griglia[17]==griglia[25]==griglia[33]==griglia[41] and griglia[17]!=" ":
        vittoria = True
    elif griglia[16]==griglia[24]==griglia[32]==griglia[40] and griglia[16]!=" ":
        vittoria = True
    elif griglia[15]==griglia[23]==griglia[31]==griglia[39] and griglia[15]!=" ":
        vittoria = True
    elif griglia[14]==griglia[22]==griglia[30]==griglia[38] and griglia[14]!=" ":
        vittoria = True
    elif griglia[2]==griglia[10]==griglia[18]==griglia[26] and griglia[2]!=" ":
        vittoria = True
    elif griglia[9]==griglia[17]==griglia[25]==griglia[33] and griglia[9]!=" ":
        vittoria = True
    elif griglia[8]==griglia[16]==griglia[24]==griglia[32] and griglia[8]!=" ":
        vittoria = True
    elif griglia[7]==griglia[15]==griglia[23]==griglia[31] and griglia[7]!=" ":
        vittoria = True
    elif griglia[0]==griglia[8]==griglia[16]==griglia[24] and griglia[0]!=" ":
        vittoria = True
    elif griglia[1]==griglia[9]==griglia[17]==griglia[25] and griglia[1]!=" ":
        vittoria = True

    return vittoria

def isLibera(griglia, n):
    """funzione che controlla che la cella che si vuole occupare è libera"""
    libero = False
    if colonne[n] < 5:
        libero = True
    return libero

def disegnaGriglia(griglia):
    print("\n\n")
    k = 35
    while (k >= 0):
        print(" " + (griglia[k]) + " | " + (griglia[k+1]) + " | " + (griglia[k+2]) + " | " + (griglia[k+3]) + " | " + (griglia[k+4]) + " | " + (griglia[k+5]) + " | " + (griglia[k+6]) + " ")
        print(f"---------------------------")
        k -= 7


def controlloPareggio(griglia):
    libera = False
    k = 0
    while libera == False and k <= 8:
        if griglia[k] == " ":
            libera = True
        k += 1

    return libera

griglia = {0:" ", 1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" ", 10:" ", 11:" ", 12:" ", 13:" ", 14:" ", 15:" ",
                16: " ", 17:" ", 18:" ", 19:" ", 20:" ", 21:" ", 22:" ", 23:" ", 24:" ", 25:" ", 26:" ", 27:" ", 28:" ", 29:" ",
                30:" ", 31:" ", 32:" ", 33:" ", 34:" ", 35:" ", 36:" ", 37:" ", 38:" ",  39:" ", 40:" ", 41:" "}
disegnaGriglia(griglia)

colonne = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

win = controlloVittoria(griglia)
while(True):
    sceltaA = int(input("O inserisce il numero della colonna in cui infilare la pedina: "))
    while ((sceltaA >= 0 and sceltaA < 7) and (isLibera(griglia, sceltaA) == False)):
        sceltaA = int(input("O inserisce il numero della colonna in cui infilare la pedina: ")) 

    griglia[(sceltaA + (7*colonne[sceltaA]))] = "O"
    colonne[sceltaA] += 1    
    disegnaGriglia(griglia)
    win = controlloVittoria(griglia)
    if win == True:
        print("Ha vinto O!")
        sys.exit()
    elif controlloPareggio == False:
        print("Pareggio")
        sys.exit()
        
    sceltaB = int(input("X inserisce il numero della colonna in cui infilare la pedina: "))
    while ((sceltaB >= 0 and sceltaB < 7) and (isLibera(griglia, sceltaB) == False)):
        sceltaB = int(input("X inserisce il numero della colonna in cui infilare la pedina: ")) 

    griglia[(sceltaB + (7*colonne[sceltaB]))] = "X"
    colonne[sceltaB] += 1    
    disegnaGriglia(griglia)
    if win == True:
        print("Ha vinto X!")
        sys.exit()
    elif controlloPareggio == False:
        print("Pareggio")
        sys.exit()
