"""Creare una lambda function che ritorni True se una stringa inizia con lettera maiuscola, False altrimenti."""

maiuscola = lambda parola: True if(parola[0] >= 'A' and parola[0] <= 'Z') else False      #parola[0] == parola[0].upper

parola = input("Inserisci una parola: ")
print(maiuscola(parola))


