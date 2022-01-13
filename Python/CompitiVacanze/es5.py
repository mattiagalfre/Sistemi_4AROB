"""Scrivere un programma in Python che prenda in input il nome file di
un programma scritto in C. Il programma deve leggere il file e:
1. Contare il numero di righe totali
2. Contare il numero di chiamate alla funzione “printf”
3. Contare il numero di linee di commento."""

nomeFile = input("Inserisci il nome del file su cui vuoi lavorare: ")
percorso = "./" + nomeFile

f = open(percorso, "r")
righe = f.readlines()
f.close()

numRighe = 0
numPrintf = 0
numCommenti = 0
for riga in righe:
    numRighe += 1
    if "printf" in riga:
        numPrintf += 1
    numCommenti += riga.count("//")
    numCommenti += riga.count("/*")
    

print(f"Il file ha {numRighe} righe")
print(f"Il file richiama {numPrintf} volte la funzione printf")
print(f"Il file contiene {numCommenti} commenti")