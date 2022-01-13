import random       #includo la libreria random per poterne poi usare le funzioni

def spostamentoCasuale():               #funzione che mi restituisce -1 oopure 1 in modo casuale, escludendo lo 0
    spostamento = random.randint(-1, 1)
    while spostamento == 0:
        spostamento = random.randint(-1, 1)
    return spostamento;

nSpostamenti = 60*60*24*5           #calcolo degli spostamenti: secondi * minuti * ore * giorni

spostamenti = [spostamentoCasuale() for _ in range(nSpostamenti+1)]     #list comprehension che assegna lo spostamento progressivamente nella lista
#print(spostamenti)

sommaSpostamenti = 0
for spostamento in spostamenti:         #calcolo la somma degli spostamenti con un ciclo
    sommaSpostamenti = sommaSpostamenti + spostamento

print(sommaSpostamenti)     #stampo la somma

