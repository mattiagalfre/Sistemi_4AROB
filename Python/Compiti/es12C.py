"""Scrivi un programma in Python che permetta all’utente di inserire un numero intero e una stringa: 
concatena la stringa con sé stessa tante volte quante il numero e stampa il risultato."""

num = int(input("Inserisci un numero: "))
stringa = input("Inserisci una stringa: ")
stringaConcat = ""

stringConcat = stringa * num
print(stringConcat)