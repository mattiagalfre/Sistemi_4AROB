"""Calcola, mediante un opportuno programma in Python, quanti sono i numeri primi minori di 1000. 
Per stabilire se il numero è primo crea una funzione apposita che ritorni True se il numero è primo, False altrimenti"""

def isPrimo(n):
    primo=True 
    k = 2
    while (k < n/2 and primo == True):
        if(n%k == 0):
            primo = False
        k = k + 1
    return primo

numeriPrimi = 0
lista = []

primi = [k for k in range(2, 1003) if isPrimo(k)]       #LIST COMPREHENSION
"""
for k in range(1000):
    if(isPrimo(k) == True):
        numeriPrimi = numeriPrimi + 1
        lista.append(k)

print(f"Ci sono {numeriPrimi} numeri primi minori di 1000")
print(lista)"""
print(primi)