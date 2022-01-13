"""Scrivi un programma in Python in cui chiedi all’utente un numero e comunichi se esso è primo oppure no. 
Per stabilire se il numero è primo crea una funzione apposita che ritorni True se il numero è primo, False altrimenti"""

def isPrimo(n):
    primo=True 
    k = 2
    while (k < n/2 and primo == True):
        if(n%k == 0):
            primo = False
        k = k + 1
    return primo

numero = int(input("Inserisci un numero: "))
if(isPrimo(numero) == True):
    print(f"{numero} è un numero primo")
else:
    print(f"{numero} non è un numero primo")
