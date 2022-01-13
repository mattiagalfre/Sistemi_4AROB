"""Scrivi un programma Python che salvi su un file i primi 100 numeri primi, uno per ogni riga del file"""

def isPrimo(n):
    primo=True 
    k = 2
    while (k < (n+1)/2 and primo == True):
        if(n%k == 0):
            primo = False
        k = k + 1
    return primo

f = open("./numeriPrimi.txt", "w")

j = 0
numero = 1
while(j <= 100):
    if(isPrimo(numero) == True):
        f.write(f"{numero}\n")
        j += 1
    numero += 1

f.close()