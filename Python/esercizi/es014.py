"""Scrivi un programma in Python in cui chiedi all’utente un numero e 
comunichi se esso è divisibile per 2, oppure per 3, oppure per 5, oppure per nessuno di essi."""

num = int(input("Inserisci un numero: "))

if num%2 == 0:
    print("Il numero è divisibile per 2 \n")
elif num%3 == 0:
    print("Il numero è divisibile per 3 \n")
elif num%5 == 0:
    print("Il numero è divisibile per 5 \n")
else:
    print("Il numero non è divisibile per 2, 3, 5 \n")

   

