"""Creare una lambda function che ritorni True se una stringa è palindroma, False altrimenti."""

palindroma = lambda parola: parola == parola[::-1]

parola = input("Inserisci una parola: ")
print(palindroma(parola))