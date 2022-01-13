"""Utilizzando le list comprehension scrivi un programma 
che crei una lista con tutte le potenze di due minori o uguali a un valore inserito dall’utente. Stampa la lista. """
import math

potenze = [k for k in range(int(input("inserisci un numero: "))) if math.sqrt(k)%2 == 0]
print(potenze)