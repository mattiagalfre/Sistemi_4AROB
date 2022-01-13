"""Crea un programma Python che permetta all'utente di inserire un numero qualunque 
di interi all'interno di una lista. Stampa la lista al termine dell'inserimento."""

risposta = "si"
elenco = []
while(risposta == "si"):
    num = int(input("Inserisci il numero da aggiungere alla lista: "))
    elenco.append(num)
    risposta = input("Vuoi inserire altri numeri? ('si' per continuare)\n")
print(elenco)