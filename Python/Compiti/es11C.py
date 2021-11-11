"""Scrivi un programma in Python che permetta all’utente di inserire due numeri qualsiasi. 
Crea una lista contenente: la somma dei quadrati dei due numeri Il quadrato della somma dei numeri la differenza tra i quadrati 
dei due numeri la differenza tra i numeri al quadrato Stampa la lista ottenuta."""

n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
lista = []
lista.append((n1**2)+(n2**2))
lista.append((n1+n2)**2)
lista.append((n1**2)-(n2**2))
lista.append((n1-n2)**2)
print(lista)